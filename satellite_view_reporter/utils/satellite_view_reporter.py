from requests import get, __version__
import os, re, reverse_geocoder as rg


class Satellite_View_Reporter:
    """Module to download S3 data for downloading MERRA (Modern-Era Retrospective analysis for Research and Applications).
    """


    def __init__(self, feature_to_visualize='LWGNTICE', year='2018', month='09', day='01'):
        """Intialize the object to retrieve MERRA data using OPeNDAP Software.

        Args:
            feature_to_visualize (str, optional): Specific Feature to visualize. Defaults to 'LWGNTICE'.
            year (str, optional): Year. Defaults to '2018'.
            month (str, optional): Month. Defaults to '09'.
            day (str, optional): Day. Defaults to '01'.
        """
        self.REQ_FORMAT = 'ascii'
        self.BASE_URL = 'https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/'
        self.MERRA2_version = '5.12.4'
        self.COLLECTION_SHORTNAME = 'M2T1NXOCN' if feature_to_visualize=='LWGNTICE' else 'M2T1NXRAD'
        self.COLLECTION_LONGNAME  = 'tavg1_2d_ocn_Nx' if feature_to_visualize=='LWGNTICE' else 'tavg1_2d_rad_Nx'
        self.COLLECTION_NUMBER = 'MERRA2_401' if year=='2020' and month=='09' else 'MERRA2_400'
        self.YEAR = year
        self.MONTH = month
        self.DAY = day
        self.FEATURE = feature_to_visualize
        self.TIME_WINDOWS = '[0:4:23]' # 24 hours divided into 6 hour chunks
        self.LAT_WINDOWS = '[0:5:360]' # 360 deg latitudes divided into 120 chunks
        self.LONG_WINDOWS = '[0:5:575]' # 575 deg longitudes divided into 115 chunks
        self.PARAMS_TO_RECEIVE = [
                self.FEATURE+self.TIME_WINDOWS+self.LAT_WINDOWS+self.LONG_WINDOWS, 
                'lat'+self.LAT_WINDOWS, 
                'lon'+self.LONG_WINDOWS, 
                'time'+self.TIME_WINDOWS
                ]
        
    
    
    def check_params_valid(self):
        """Checks if request-parameters are as per expectation, 'visualize' parameter has appropriate value.

        Returns: 0 if invalid, 1 if valid
        """
        if None in [self.FEATURE, self.YEAR, self.DAY, self.MONTH] or self.FEATURE not in ['LWGNTICE', 'ALBEDO']:
            return 0
        return 1




    def set_write_parameters(self, target_folder):
        """Sets the relative-path of file where we want to write the MERRA data's subset.

        Args:
            target_folder (str): Folder location

        Returns:
            filename (str): Relative path to write the target file.
        """
        unique_tgt_filename = os.path.join(target_folder, '_'.join([self.COLLECTION_SHORTNAME, self.FEATURE, self.YEAR, self.MONTH, self.DAY]))+'.txt'
        return unique_tgt_filename





    def set_search_parameters(self):
        """Sets the folder to search via OPeNDAP, based on request params.
        Sets the filename parameters to search and download, based on request params.

        Returns:
            folder_url (str): Absolute path of OPeNDAP folder to search.
        """
        folder_url = f'{self.BASE_URL}{self.COLLECTION_SHORTNAME}.{self.MERRA2_version}/{self.YEAR}/{self.MONTH}/'
        file_url = f'{self.COLLECTION_NUMBER}.{self.COLLECTION_LONGNAME}.{"".join([self.YEAR,self.MONTH,self.DAY])}.nc4.{self.REQ_FORMAT}'
        return folder_url+file_url






    def create_path_if_not_exist(self, folder, verbose=True):
        """Checks if input path exists, and creates the directory if required.

        Args:
            folder (str): [description]
            verbose (bool, optional): Flag to indicate whether to print logs in verbose mode. Defaults to False.
        Returns:
            [int]: 0 if path already exists, 1 if path created just now.
        """    
        if not os.path.exists(folder):
            if verbose:  print(f'Path doesnt exist. Creating it now... {folder}')
            os.makedirs(folder)
            return 1
        return 0






    def download_merra_subset(self, download_data_dir, verbose=True):
        """Retrieves a subset of MERRA data using OPeNDAP.
        Adds 'ascii' between url and request-params.
        Sample URL: 'https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXOCN.5.12.4/2018/09/MERRA2_400.tavg1_2d_ocn_Nx.20180906.nc4.ascii?LWGNTICE[0:1:23][0:1:360][0:1:575],lat[0:1:360],lon[0:1:575],time[0:1:23]'
        
        Args:
            download_data_dir (str): Parent-folder where to download the dataset.
            verbose (bool, optional): Flag to indicate whether to print logs in verbose mode. Defaults to False.
        Returns:
            abs_path (str): Absolute path where raw-dataset is stored.
        """
        TGT_FOLDER = os.path.join(download_data_dir)
        _ = self.create_path_if_not_exist(TGT_FOLDER)

        url = self.set_search_parameters()
        url_params = f'{",".join(self.PARAMS_TO_RECEIVE)}'
        if verbose:  print(f'url={url} \nurl_params={url_params}')

        target_filename = self.set_write_parameters(TGT_FOLDER)
        response = get(url=url, params=url_params)
        response.raise_for_status()
        with open(target_filename, 'wb') as f:
            f.write(response.content)
            if verbose:  print(f'Written file to {target_filename}')
        print('Data Ingestion complete...')
        return target_filename






    def convert_response_to_json(self, filename='temp.txt', verbose=False):
        """Converts the raw MERRA-data .txt file into json

        Args:
            filename (str, optional): Absolute path where raw-dataset is stored. Defaults to 'temp.txt'.
            verbose (bool, optional): Flag to indicate whether to print logs in verbose mode. Defaults to False.

        Returns:
            json_data: Parsed version of raw-dataset.
        """
        data = None
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.readlines()

        json_data = {}
        for line in data[1:]:
            parts = line.split(',')
            key, values = parts[0], [value.strip() for value in parts[1:]]
            json_data[key] = values
        if verbose:  print(json_data.keys())
        return json_data




    def get_country_measurements(self, locations_vs_measurements, verbose=False):
        """Converts lat-long locations into country-codes.
        Normalizes the measurements.
        We're looking at only one timestep within this function.

        Args:
            locations_vs_measurements (dict): Hashmap of (lat,long) vs measurement captured.
            verbose (bool, optional): Flag to indicate whether to print logs in verbose mode. Defaults to False.

        Returns:
            country_measurements (dict): Hashmap of (country_code, avg_measurement).
        """
        if verbose:  print('Creating a {country:(sum,count)} dictionary...')
        country_measurements = dict()
        all_locations = list(locations_vs_measurements.keys())
        all_locations_mapped = rg.search(all_locations)
        for loc, country in zip(all_locations, all_locations_mapped):
            if verbose:  print(loc, country['cc'], locations_vs_measurements[loc])
            if country['cc'] not in country_measurements:
                country_measurements[country['cc']] = [0,0]
            country_measurements[country['cc']][0] += locations_vs_measurements[loc][0]
            country_measurements[country['cc']][1] += 1

        if verbose:  print('Normalizing the measurements taken for each country...')
        total = 0
        for country, (tot,cnt) in country_measurements.items():
            country_measurements[country] = tot/cnt
            total += country_measurements[country]

        for country, val in country_measurements.items():
            country_measurements[country] = (val/total)*100

        return country_measurements




    def parse_json_dataset(self, json_data, verbose=False):
        """For each timestep, identifies the relevant keys in the raw-dataset.
        For these keys, creates a hashmap of {(latitude,longitude):measurement}.
        Converts lat,long to country-code using get_country_measurements().
        Returns final data-format for visualizing on React.

        Args:
            json_data (dict): Parsed json-format of raw-dataset.
            verbose (bool, optional): Flag to indicate whether to print logs in verbose mode. Defaults to False.

        Returns:
            json_res (dict): Final parsed data-format to be used for visualization on React.
        """
        json_res = dict()
        for t, time_val in enumerate(json_data['time']):
            if verbose:  print(f'Getting measurements across all (latitudes,longitudes) within timestep {time_val}..')
            latitude_rows = []
            for k in json_data.keys():
                if re.findall(f'\[{t}\]\[.*\]', k):
                    if verbose:  print(k)
                    latitude_rows.append(k)

            locations_vs_measurements = dict()
            for i,latitude_row in enumerate(latitude_rows):
                latitude = int(float(json_data['lat'][i]))
                longitudinal_measurements = json_data[latitude_row]
                for j, measurement in enumerate(longitudinal_measurements):
                    longitude = int(float(json_data['lon'][j]))
                    location = (latitude,longitude)
                    if location not in locations_vs_measurements:
                        locations_vs_measurements[location] = []
                    locations_vs_measurements[location].append(100 if measurement=='1e+15' else float(measurement))
            json_res[time_val] = self.get_country_measurements(locations_vs_measurements, verbose=False)

        return json_res