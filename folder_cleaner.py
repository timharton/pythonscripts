#!/usr/bin/python
# folder_cleaner.py

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

# Selecting all the files in current path including sub directories
files  = [f for f in os.walk('.') if os.path.isfile(f)]
for  in files:
    print os.stat(fpath)
    
