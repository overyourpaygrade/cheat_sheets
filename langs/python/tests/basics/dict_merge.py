#!/usr/bin/env python
#https://www.reddit.com/r/learnpython/comments/4ch6s6/how_to_merge_two_dictionaries_without_overwriting/

from collections import defaultdict

d1 = {'boy' : 1, 'girl' : 2}
d2 = {'boy' : 'tall', 'girl' : 'short'}
d3 = defaultdict(list)

for d in (d1, d2):
    for key, value in d.items():
        d3[key].append(value)


print d3

print dict(d3)


'''
---------------------------------------------
'''

d3_mod = {k: (d1[k],v) for k, v in d2.iteritems() if k in d1}

print d3_mod
