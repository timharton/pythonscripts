# test_folder_cleaner.py

import unittest

from os import mkdir, removedirs 
from os.path import join

from folder_utils import Folder

"""
Author: Tim Harton, tim@harton.co
Date: 2013-08-15
"""

def setUp(self):
    """
    """
    self.test_path = 'test_dir'
    mkdir(self.test_path)
    mkdir(join(self.test_path+'test_dir1'))
    for i in range(10)
        file_path = 'test_file'+i
        open(join(self.test_path,file_path), 'a').close()
    self.folder = Folder(self.test_path)

def tearDown(self):
    """
    """
    removedirs(self.test_path)

def find_files(self):
    """
    Tests the find_files function in folder_cleaner.py. It does thid through
    creating a directory and sub directories with 
    """
    pass

