import warnings, json, sys
warnings.filterwarnings('ignore')
from siphon.radarserver import RadarServer
from pprint import pprint



class Radar_Stations:
    """Module to access S3 data for NEXRAD (Next Generation Radar) weather monitoring and retrieve metadata of stations.
    """

    def __init__(self, verbose=False):
        """Intialize the object to retrieve weather radar stations using siphon server.
        Args:
            verbose (bool, optional): Flag to capture logs in detail. Defaults to False.
        """
        self.BASE_URL = 'http://tds-nexrad.scigw.unidata.ucar.edu/thredds/'
        self.LEVEL_II_NEXRAD_DATA = 'radarServer/nexrad/level2/S3/'
        self.verbose = verbose



    def get_stations(self):
        """Creates a list of bucket-items present on S3 with a specified prefix-pattern. Loops through these potential candidates to identify the best filename which matches HOUR and MINUTE.
        Returns:
            [dict]: A json-object with metadata for all radar-stations monitored as part of NEXRAD.
        """
        self.rs = RadarServer(self.BASE_URL+self.LEVEL_II_NEXRAD_DATA)
        locations = {}
        for station, v in self.rs.stations.items():
            loc_name = v.name.split('/')[0]
            if loc_name not in locations:
                locations[loc_name] = []
            locations[loc_name].append([v.name.split('/')[-1], station])
            if self.verbose:
                if station=='kvnx'.upper():
                    print('  ->  '.join(map(str,[station, v.elevation, v.latitude, v.longitude, v.name])))
        
        pprint(locations)
        return locations


    def get_stations_bytestream(self, stations_list):
        print('Converting the dictionary to bytes...')
        stations_str = json.dumps(stations_list)
        print('Converted the dictionary to string...')
        stations_buffer = bytes(stations_str, encoding='utf-8')
        print(f'Original Size of image bytestream will be {sys.getsizeof(stations_buffer)}')
        return stations_buffer