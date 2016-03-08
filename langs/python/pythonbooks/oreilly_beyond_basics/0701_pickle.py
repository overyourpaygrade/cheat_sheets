#!/usr/bin/env python

import pickle

mylist = ['a', 'b', 'c', 'd']

with open('0701_datafile.txt', 'w') as fh:
    pickle.dump(mylist, fh)

with open('0701_datafile.txt') as fh:
    unpickledlist = pickle.load(fh)

print unpickledlist
