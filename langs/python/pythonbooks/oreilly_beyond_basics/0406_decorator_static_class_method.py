#!/usr/env/bin python

class InstanceCounters(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)
