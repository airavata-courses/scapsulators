from random import random
import shutil
import unittest
from utils.weather_reporter import Weather_Reporter


class Testing(unittest.TestCase):

    def test1(self):
        """Check for valid params setting
        """
        wr = Weather_Reporter(feature_to_visualize="reflectivity", station="KVNX", year="2018", month="12", day="25", hour="09", minute="23")
        self.assertEqual(wr.check_params_valid(), 1)


    def test2(self):
        """Check for invalid params setting
        """
        wr = Weather_Reporter(feature_to_visualize="reflex", station="KVNX", year="2018", month="12", day="25", hour="09", minute="23")
        self.assertEqual(wr.check_params_valid(), 0)


    def test3(self):
        """Check for random folder creation
        """
        random_folder_name = 'Temp'+str(int(random()*100))
        wr = Weather_Reporter(feature_to_visualize="reflectivity", station="KVNX", year="2018", month="12", day="25", hour="09", minute="23")
        status = wr.create_path_if_not_exist(random_folder_name)
        self.assertEqual(status, 1)
        shutil.rmtree(random_folder_name)


    def test4(self):
        """Check for existence of S3 object
        """
        wr = Weather_Reporter(feature_to_visualize="reflectivity", station="KVNX", year="2018", month="12", day="25", hour="09", minute="23")
        s3_object = wr.get_s3_object(True)
        expected_file_name = '2018/12/25/KVNX/KVNX20181225_000452_V06'
        self.assertEqual(s3_object.key, expected_file_name)
        


if __name__=='__main__':
    unittest.main()