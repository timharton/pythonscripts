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

def find_files(tree_search=True):
    """
    Finds all the files in the current directory
    Input:  tree_search-  search subtrees or not
    Output; files all the files found
    """
    files = []
    return files

# Selecting all the files in current path including sub directories
files  =  [files for root, dirs, files in os.walk('.')]
for f in files:
    #print os.stat(f)
    print f
    
        
