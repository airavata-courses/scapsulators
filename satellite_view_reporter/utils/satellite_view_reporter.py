from requests import get, __version__
import os


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
        self.COLLECTION_SHORTNAME = 'M2T1NXOCN'
        self.COLLECTION_LONGNAME  = 'tavg1_2d_ocn_Nx'
        self.COLLECTION_NUMBER = 'MERRA2_401' if year=='2020' and month=='09' else 'MERRA2_400'
        self.YEAR = year
        self.MONTH = month
        self.DAY = day
        self.FEATURE = feature_to_visualize
        self.TIME_WINDOWS = '[0:6:23]' # 24 hours divided into 6 hour chunks
        self.LAT_WINDOWS = '[0:1:360]' # 360 deg latitudes
        self.LONG_WINDOWS = '[0:1:575]' # 575 deg longitudes
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
        if None in [self.FEATURE, self.YEAR, self.DAY, self.MONTH] or self.FEATURE not in ['LWGNTICE']:
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