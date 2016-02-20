#!/usr/bin/env python

def bar():
    return "foo bar"

mydct = {
    'foo': bar,
    'moo': 'meow'
    }

dct = {
    'foo': 'bar',
    'moo': 'meow',
    'raw': 'rawr'
    }

print mydct['foo']()

# Delete one item by key
del mydct['moo']

# Clear all entries
mydct.clear()

# Delete the dictionary
del mydct

# Iterate over dictionary
for k,v in dct.iteritems():
    print k, v


