#!/usr/bin/python
#folder_cleaner.py

import os

"""
This script will be run on a regular basis either through cron or another
scheduler. 
It will cleanup a folder based on timerange selected. Any files create within
that time range will be left alone. All others will be deleted. If they are too
old they will be deleted.

Author: Tim Harton, tim@harton.co
Date: 2013-08-14
"""

class Folder():
    """
    A Class which provides utilities for file cleanup.
    """
    def __init__(self, path='.'):
        self.path = path 

    def find_files(self, tree_search=True):
        """
        Finds all the files in the current directory
        Input:  tree_search-  search subtrees or not
        Output; files all the files found
        """
        files = []
        if tree_search:
            # Selecting all the files in current path including sub directories
            filelists  =  [files for root, dirs, files in os.walk(self.path)]
            files = [f for f_list in filelists for f in f_list]
            for f in files:
                    
            
            #print [f for f in 
            #for file_list in filelists:
            #    for f in file_list:
            #                print f
    
        return files

if __name__ == "__main__":
    folder = Folder()
    folder.find_files()
