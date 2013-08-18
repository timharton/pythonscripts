# utils/files.py

import os

"""
Utilities for dealing with files

Author: Tim Harton. tim@harton.co
Date: 2013-08-18
"""

def touch(file_path):
    """
    Replicates the touch command in bash with python.
    
    Inputs: file_path
    """
    # Takes the path and turns it into the directories path
    basedir = os.path.dirname(path)
    
    # mkdir if it doesn't exist
    if not os.path.exists(basedir):    
        os.makedirs(basedir)
    
    # Creates file or appends if already exits
    with open(path, 'a'):
        os.utime(path, None)

    return
