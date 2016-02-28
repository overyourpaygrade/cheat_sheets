#!/usr/bin/env python

class MyDict(dict):

    def __setitem__(self, key, val):
        print "Setting a key and value!"
        dict.__setitem__(self, key, val)


dd = MyDict()
dd['a'] = 5
dd['b'] = 6


for key in dd.keys():
    print('{0}={1}'.format(key, dd[key]))

print
