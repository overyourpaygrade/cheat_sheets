#!/usr/bin/env python3

class YourClass(object):
    classy = 10

    def set_val(self):
        self.insty = 100

dd = YourClass()

dd.set_val()

print(dd.classy)
print(dd.insty)
print()

# Instance has access to class attributes 
# and instance attributes
# Lookup first in the instance then in the class
# This is called attrib lookup order

class MyClass(object):
    classy = 'class value!'

dd = MyClass()
print(dd.classy)

dd.classy = 'inst value!'
print(dd.classy)

del dd.classy
print(dd.classy)
