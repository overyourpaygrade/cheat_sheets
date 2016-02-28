#!/usr/bin/env python

class SumList(object):

    def __init__(self, this_list):
        self.mylist = this_list

    def __add__(self, other):

        new_list = [ x + y for x, y in zip(self.mylist, other.mylist) ]

        # following 4 lines same as line above
        # new_list = []
        # zipped_list = zip(self.mylist, other.mylist)
        # for tup in zipped_list:
        #   new_list.append(tup[0] + tup[1])

        return SumList(new_list)

    def __repr__(self):
        return str(self.mylist)

cc = SumList([1, 2, 3, 4, 5])
dd = SumList([100, 200, 300, 400, 500])

ee = cc + dd    # cc.__add__(dd)
print ee        # should give us [101, 202, 303, 404, 505]
