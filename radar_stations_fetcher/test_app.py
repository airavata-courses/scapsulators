import unittest
from utils.radar_stations import Radar_Stations


class Testing(unittest.TestCase):

    def test1(self):
        """Check for proper response of geographic-locations -> radar-station.
        """
        radar_stations = Radar_Stations()
        self.assertIsInstance(radar_stations.get_stations(), dict)


if __name__=='__main__':
    unittest.main()