from unittest import TestCase
import wget
import os
import zipfile
#  TEST
from os_helper import *


def download_files_to_test():
    if not os.path.exists('download'):
        os.makedirs('download')

    if not os.path.exists('download/101_food_classes_10_percent.zip'):
        print("downloading ZIP")
        url = 'https://storage.googleapis.com/ztm_tf_course/food_vision/101_food_classes_10_percent.zip'
        zip_file = wget.download(url, 'download')

    if not os.path.exists('download/test_images'):
        os.makedirs('download/test_images')
        with zipfile.ZipFile('download/101_food_classes_10_percent.zip', 'r') as zip_ref:
            zip_ref.extractall('download/test_images/')
    print('Downloaded Images')


class TestOsHelper(TestCase):

    def test_info_dir(self):
        download_files_to_test()
        images = info_dir('download')
        self.assertGreater(len(images), 0, "ERROR len of data == 0")
        self.assertIsInstance(images, list, "ERROR not list")
