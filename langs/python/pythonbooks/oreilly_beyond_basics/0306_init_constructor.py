#!/usr/bin/env python3

class MyNum(object):
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value

    def increment(self):
        self.val = self.val + 1

aa = MyNum('hello')  # Calling __init__
bb = MyNum(100)      # Calling __init__
aa.increment()
aa.increment()
bb.increment()

print(aa.val)
print(bb.val)
