from unittest import TestCase
from retrieve_data import *
from os_helper import delete_file

import os

download_folder = "./download"


class Test(TestCase):

    def test_download(self,):
        file_name = "101_food_classes_10_percent"
        delete_file(f"{download_folder}/{file_name}")

        url = "https://storage.googleapis.com/ztm_tf_course/food_vision/101_food_classes_10_percent.zip"
        get_zipped_content_url(url, f"{download_folder}")

