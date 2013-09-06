# utils/tests/test_files.py

import os
import unittest

from utils import files

"""
Test functions for utils.files

Author: Tim Harton, tim@harton.co
Date:   2013-06-18
"""

TEST_PATH = 'test_dir'
class FileTests(unittest.TestCase):

    def setUp(self):
        """
        Sets up environmment for testing
        """
        self.TEST_PATH = 'test_file'
        if not os.path.exists(self.TEST_PATH):
            os.mkdir(self.TEST_PATH)

    def tearDown(self):
        """
        Tears down the environment after testing
        """
        os.remove(self.TEST_PATH)

    def test_touch(self):
        """
        Test function for utils.files.touch
        """
        # Check file doesn't exist then it is created
        with self.assertRaises(OSError):
            fid = open(self.TEST_PATH, 'r')

        files.touch(self.TEST_PATH)
        # Check file doesn't change other than mod date if it already exists

        # Check that new directories are made if they don't exist
        pass
