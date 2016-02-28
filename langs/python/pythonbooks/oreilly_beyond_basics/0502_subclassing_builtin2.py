#!/usr/bin/env python

# Mylist inherits from "list" object but indexes from 1 instead of 0!

class MyList(list):     # inherit from list

    def __getitem__(self, index):
        if index == 0: raise IndexError
        if index > 0: index = index - 1
        return list.__getitem__(self, index) # this method is called when we access
                                             # a value with subscript (x[1], etc.)
    def __setitem__(self, index, value):
        if index == 0: raise IndexError
        if inex > 0: index = index - 1
        list.__setitem__(self, index, value)

x = MyList(['a', 'b', 'c'])     # __init__() inherited from builtin list

print x                         # __repr__() inherited from builtin list

x.append('spam')                # append() inherited from builtin list

print x[1]                      # 'a' (MyList.__getitem__
                                #      customizes list superclass method)
print x[4]                      # 'spam' (index is 4 but reflects 3!)
