#!/usr/bin/env python3

import random

class MyClass(object):
    def dothis(self):
        self.rand_val = random.randint(1,10)

myinst = MyClass()

myinst.dothis()

print(myinst.rand_val)
