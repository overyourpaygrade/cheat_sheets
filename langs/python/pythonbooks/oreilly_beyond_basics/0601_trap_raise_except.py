#!/usr/bin/env python

import sys

try:
    arg = sys.argv[1]
    num = int(arg)
except(IndexError, ValueError):
    exit('please enter an integer on the command line')

print "thanks for the int"

mydict = {'a':1, 'b':2}

try:
    print 5/0
except ZeroDivisionError, e:
    print e.message
    print e.args
