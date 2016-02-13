#!/usr/bin/env python

import fnmatch
import os

# Find all pdf files
rootPath = '/'
pattern = '*.pdf'

for root,dirs,files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))


# Find files that match
images = ['*.jpg','*.jpeg','*.png','*.tif','*.tiff']
matches = []

for root,dirnames,filenames in os.walk(rootPath):
    for extensions in images:
        for filename in fnmatch.filter(filenames,extensions):
            matches.append(os.path.join(root,filename))

for match in matches:
    print match
