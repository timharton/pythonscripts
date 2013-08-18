#!/usr/bin/python
#folder_cleaner.py

from os import walk, listdir
from os.path import join, isfile

"""
This script will be run on a regular basis either through cron or another
scheduler. 
It will cleanup a folder based on timerange selected. Any files create within
that time range will be left alone. All others will be deleted. If they are too
old they will be deleted.

Author: Tim Harton, tim@harton.co
Date: 2013-08-14
"""

def find_files(self, tree_search=True):
    """
    Finds all the files in the current directory
    Input:  tree_search-  search subtrees or not
    Output; files all the files found
    """
    file_paths = []
    if tree_search:
        # Selecting all the files in current path including sub directories
        for root, dirs, files in walk(self.path):
            for f in files:
                file_paths.append(join(root, f))
        
    else: 
        for f in listdir(self.path):
            file_path = join(self.path,f)
            if isfile(file_path):
                file_paths.append(file_path)
    
    return file_paths
