# utils/tests/test_files.py

import os

from utils import files

"""
Test functions for utils.files

Author: Tim Harton, tim@harton.co
Date:   2013-06-18
"""

TEST_PATH = 'test_dir'

def setUp():
    """
    Sets up environmment for testing
    """
    if not os.path.exists(TEST_PATH):
        os.mkdir(TEST_PATH)

def tearDown():
    """
    Tears down the environment after testing
    """
    os.removedirs(TEST_PATH)

def test_touch():
    """
    Test function for utils.files.touch
    """
    # Check file doesn't exist then it is created

    # Check file doesn't change other than mod date if it already exists
    
    # Check that new directories are made if they don't exist
    pass
