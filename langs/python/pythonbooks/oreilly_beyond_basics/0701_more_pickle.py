#!/usr/bin/env python

import pickle

this_int = 555
this_string = 'oh my goodness'
mydict_of_lists = {
    'a': [1, 2, 3],
    'b': [4, 5, 6]
}

query_results = [('joe', 22, 'clerk'), ('pete', 34, 'salesman')]

with open('0701_more_datafile.txt', 'w') as fh:
    pickle.dump((this_int, this_string, mydict_of_lists, query_results), fh)

with open('0701_more_datafile.txt') as fh:
    tup = pickle.load(fh)

print tup[0]
print tup[1]
print tup[2]
print tup[3]
