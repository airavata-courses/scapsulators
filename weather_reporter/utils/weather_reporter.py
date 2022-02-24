# Pyart is compatible only with Python 3.8x
import os, pyart, imageio, warnings, matplotlib.pyplot as plt, shutil, io
warnings.filterwarnings('ignore')
from boto.s3.connection import S3Connection
from PIL import Image



class Weather_Reporter:
    """Module to download S3 data for NEXRAD (Next Generation Radar) weather monitoring and GIF image generation.
    """


    def __init__(self, feature_to_visualize='reflectivity', station='KVNX', year='2011', month='05', day='20', hour='10', minute='59'):
        """Intialize the object to visualize weather report as GIF image.

        Args:
            feature_to_visualize (str, optional): Defaults to 'reflectivity'.
            station (str, optional): Defaults to 'KVNX'.
            year (str, optional): Defaults to '2011'.
            month (str, optional): Defaults to '05'.
            day (str, optional): Defaults to '20'.
            hour (str, optional): Defaults to '10'.
            minute (str, optional): Defaults to '59'.
            
        """

        self.FEATURE_TO_VISUALIZE = feature_to_visualize
        self.STATION = station
        self.YEAR = year
        self.MONTH = month
        self.DAY = day
        self.HOUR = hour
        self.MINUTE = minute
        self.my_prefix = '/'.join([self.YEAR, self.MONTH, self.DAY, self.STATION])+'/'
        self.conn = S3Connection(anon=True)
        self.bucket = self.conn.get_bucket('noaa-nexrad-level2')
        self.gif_abs_path = ''
    
    
    
    def check_params_valid(self):
        """Checks if request-parameters are as per expectation, 'visualize' parameter has appropriate value.

        Returns: 0 if invalid, 1 if valid
        """
        if None in [self.FEATURE_TO_VISUALIZE, self.STATION, self.YEAR, self.DAY, self.MONTH] or self.FEATURE_TO_VISUALIZE not in ['velocity', 'reflectivity', 'spectrum_width']:
            return 0
        return 1


    
    def set_search_prefix(self):
        """Generates a prefix to be searched in S3 buckets.
        
        SAMPLE PREFIX: Year/Month/Day/Station/ ==> '2011/05/20/KVNX/'
        """
        self.my_prefix = '/'.join([self.YEAR, self.MONTH, self.DAY, self.STATION])+'/'




    def get_s3_object(self, verbose=False):
        """Creates a list of bucket-items present on S3 with a specified prefix-pattern. Loops through these potential candidates to identify the best filename which matches HOUR and MINUTE.

        Args:
            verbose (bool, optional): Flag to print logs in verbose mode. Defaults to False.

        Returns:
            [S3-File]: File that most closely matches the query-parameters in terms of spatial and temporal features.
        """
        if verbose:  print(f'Starting search for: Prefix = "{self.my_prefix}", Hour = "{self.HOUR}", Minute = "{self.MINUTE}"...')
        bucket_list = list(self.bucket.list(prefix = self.my_prefix))
        
        if len(bucket_list)==0:
            if self.HOUR>'00':
                self.HOUR = str(int(self.HOUR)-1).zfill(2)
                print(f'\n\nNo potential objects found.. Reducing hour by 1 and checking again for HOUR={self.HOUR} , prefix={self.my_prefix}..')
            elif self.DAY>'00':
                self.DAY = str(int(self.DAY)-1).zfill(2)
                print(f'\n\nNo potential objects found.. Reducing day by 1 and checking again for DAY={self.DAY} , prefix={self.my_prefix}..')
            elif self.DAY=='00' and self.HOUR=='00':
                return KeyError(f'No S3 object found for this station {self.STATION}!')
            self.set_search_prefix()
            return self.get_s3_object(verbose)

        desired_s3_object = None

        for i, s3_fname in enumerate(list(bucket_list)):
            if not s3_fname.name.endswith('gz'):
                continue
            s3_timestamp = s3_fname.name.split('_')[1]

            # Found exact match of Hour+Minute for that station
            if s3_timestamp.startswith(''.join([self.HOUR, self.MINUTE])):
                if verbose:  print(i, s3_fname.key, bucket_list[i])
                desired_s3_object = s3_fname
                break
            
            # Found partial match of Hour, keep iterating until we find max minute
            if s3_timestamp.startswith(''.join([self.HOUR, self.MINUTE[0]])):
                desired_s3_object = s3_fname

        if desired_s3_object is None:
            desired_s3_object = bucket_list[0]

        if verbose:  print(f'Found desired S3 object: {desired_s3_object}...')
        return desired_s3_object






    def create_path_if_not_exist(self, folder, verbose=True):
        """Checks if input path exists, and creates the directory if required.

        Args:
            folder ([type]): [description]
            verbose (bool, optional): [description]. Defaults to True.
        Returns:
            [int]: 0 if path already exists, 1 if path created just now.
        """    
        if not os.path.exists(folder):
            if verbose:  print(f'Path doesnt exist. Creating it now... {folder}')
            os.makedirs(folder)
            return 1
        return 0






    def download_s3_object(self, download_data_dir, verbose=False):
        """Accesses the S3 Object remotely, creates a local directory for the station if doesn't exist, and saves PyArt-object there.

        Args:
            download_data_dir ([str]): Path where S3-data is to be downloaded.
        Returns:
            [PyArt-object]: Dataset of radar measurements and metadata for corresponding query.
        """
        desired_s3_object = self.get_s3_object(verbose=True)
        if isinstance(desired_s3_object, KeyError):
            return desired_s3_object

        folder_path = os.path.join(download_data_dir, 'data', self.STATION)
        
        _ = self.create_path_if_not_exist(folder_path)

        fname = desired_s3_object.name.split("/")[-1]
        file_path = os.path.join(folder_path, fname)
        if verbose:  print(f'Absolute path for storing S3 data locally: {file_path}')

        # Write current query file to file_path
        desired_s3_object.get_contents_to_filename(filename=file_path)
        # Read the queried dataset into radar
        radar = pyart.io.read(os.path.join(file_path))
        if verbose:  print(f'All documentation about Radar Data is available here...\n{radar.info()}\n\n')
        return radar



    



    def generate_images_for_animation_by_sweep(self, radar, station, tgt_folder, sweep_intervals=3, image_format='jpeg', verbose=True):
        """Generates a set of images that will be used to generate the GIF file.

        Args:
            radar ([pyart]): pyart-object got after reading the binary S3-file.
            station ([str]): Radar-Station 4-letter code.
            tgt_folder ([str]): Location where the raw images will be written.
            sweep_intervals (int, optional): Interval-size governs number of volume-scans to use for GIF-generation. Defaults to 3.
            feature_to_plot (str, optional): Can be (reflectivity, spectrum_width, velocity).
                <Reflectivity> tells how dense the atmosphere was, and how strong the reflected RADAR signal was in Decibels relative to Z.
                <Doppler-Specturm-Width> tells us how fast moisture particles are moving in atmosphere. Set of particles grouped together form one pixel on Volume-scan.
                <Radial-Velocity-of-scatterers> the "scatterers" are what causes the transmitted signal to be returned to the Radar (eg: aerosols, hydrometeors and refractive index irregularities).
                    This measurement corresponds to how fast these "scatterers" are moving away from the Radar.. Defaults to 'reflectivity'.
            image_format (str, optional): Can be (jpeg, png, gif, ...). Defaults to 'jpeg'.
            verbose (bool, optional): Used for controlling logging. Defaults to True.
            Note: PPI is Plan Position Indicator for Radar

        Returns:
            res [list(str)]: List of file-names used for generating the overall GIF.
        """
        dataset_for_sweep = radar.fields[self.FEATURE_TO_VISUALIZE]['data'].data
        range_min = dataset_for_sweep.min()
        range_max = dataset_for_sweep.max()
        res = []
        _ = plt.figure(figsize = [10,8])
        my_display = pyart.graph.RadarMapDisplay(radar)

        for sweep_i in range(0,100,sweep_intervals):
            if verbose:  print(f'Producing image for sweep={sweep_i}...')
            try:
                my_display.plot_ppi_map(self.FEATURE_TO_VISUALIZE, sweep=sweep_i, vmin=range_min, vmax=range_max, raster=True)
                file_name = f'{tgt_folder}/{station}_{sweep_i}.jpeg'
                plt.savefig(file_name)
                res.append(file_name)
            except Exception as e:
                if verbose:  print(f'Breaking from the loop. Exception={e}')
                break
            finally:
                plt.clf()
        if verbose:  print(res)
        return res
    



    
    def generate_animation(self, download_data_dir):
        """Runs the entire pipeline for weather-report generation:
        Checks if queried file already exists as a GIF image locally (Cache-hit).
        Otherwise downloads the s3-dataset, creates local directory for generating final GIF image. Removes the folder used for temporary image generation.
        Sets an attribute for absolute-path for accessing the required GIF image.

        Args:
            download_data_dir ([str]): Path where to download data: Ideally the /static/ folder within running application.
        """
        TGT_FOLDER = os.path.join(download_data_dir,'visualizations',self.STATION)
        _ = self.create_path_if_not_exist(TGT_FOLDER)

        RAW_FOLDER = os.path.join(TGT_FOLDER, 'raw')
        _ = self.create_path_if_not_exist(RAW_FOLDER)
        
        self.gif_abs_path = os.path.join(TGT_FOLDER, ''.join([self.STATION, self.FEATURE_TO_VISUALIZE, self.YEAR, self.MONTH, self.MINUTE]))+'.gif'
        if os.path.exists(self.gif_abs_path):
            return
            
        radar = self.download_s3_object(download_data_dir)
        if isinstance(radar, KeyError):
            self.gif_abs_path = KeyError('S3 Object matching input params not found!')
            return

        images_for_animation = self.generate_images_for_animation_by_sweep(radar, self.STATION, RAW_FOLDER, 3)
        imgs = [imageio.imread(img) for img in images_for_animation]
        imageio.mimwrite(self.gif_abs_path, imgs, fps=3)
        shutil.rmtree(RAW_FOLDER)






    def get_image_bytestream(self):
        """Generates the Bytes from GIF image using the absolute path within the application.

        Returns:
            [bytes]: Bytestream from GIF image.
        """
        print(f'Converting the GIF image to bytes... {self.gif_abs_path} here!')
        img = Image.open(self.gif_abs_path)
        img.seek(0)
        buffer = io.BytesIO()
        img.save(buffer, format='gif', save_all=True)
        return buffer.getvalue()