#!/usr/bin/env python

# tail a file (like tail -f)
# http://git.devdungeon.com/DevDungeon/Cookbook/blob/master/python/tailf.py

import time

def tail(f):
    f.seek(0,2) # Move to EOF
    while True:
        line = f.readline() # Try reading a new line of text
        if not line: # if nothin, sleep briefly and try again
            time.sleep(0.1)
            continue
        yield line

