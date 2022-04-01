from random import random
import shutil, unittest, os
from utils.satellite_view_reporter import Satellite_View_Reporter


class Testing(unittest.TestCase):

    def test1(self):
        """Check for valid params setting
        """
        svr = Satellite_View_Reporter(feature_to_visualize="LWGNTICE", year="2018", month="12", day="25")
        self.assertEqual(svr.check_params_valid(), 1)


    def test2(self):
        """Check for invalid params setting
        """
        svr = Satellite_View_Reporter(feature_to_visualize="ICICLE", year="2018", month="132", day="25")
        self.assertEqual(svr.check_params_valid(), 0)


    def test3(self):
        """Check for random folder creation
        """
        random_folder_name = 'Temp'+str(int(random()*100))
        svr = Satellite_View_Reporter(feature_to_visualize="LWGNTICE", year="2018", month="12", day="25")
        status = svr.create_path_if_not_exist(random_folder_name)
        self.assertEqual(status, 1)
        shutil.rmtree(random_folder_name)


    def test4(self):
        """Check for existence of S3 object
        """
        svr = Satellite_View_Reporter(feature_to_visualize="LWGNTICE", year="2018", month="12", day="25")
        s3_object = svr.download_merra_subset(download_data_dir=os.environ.get('STATIC_DIR'), verbose=True)
        expected_file_name = '2018/12/25/KVNX/KVNX20181225_000452_V06'
        self.assertEqual(s3_object.key, expected_file_name)
        


if __name__=='__main__':
    unittest.main()