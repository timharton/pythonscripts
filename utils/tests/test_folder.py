# test_folder.py

import unittest

from os import mkdir, removedirs, remove
from os.path import join

from utils import folder

"""
Author: Tim Harton, tim@harton.co
Date: 2013-08-15
"""
class FolderTests(unittest.TestCase):

    def setUp(self):
        """
        Setup for folder paackage
        """
        self.test_path = 'test_dir'
        mkdir(self.test_path)
        mkdir(join(self.test_path, 'test_dir1'))
        for i in range(10):
            file_path = 'test_file'+str(i)
            open(join(self.test_path,file_path), 'a').close()

    def tearDown(self):
        """
        Tears the folder package down
        """
        remove(self.test_path)

    def test_find_files(self):
        """
        Tests the find_files function in folder_cleaner.py. It does thid through
        creating a directory and sub directories with
        """
        print find_files(self.test_path)
        pass

