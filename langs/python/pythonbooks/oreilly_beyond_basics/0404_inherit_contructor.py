#!/usr/bin/env python

import random

class Animal(object):
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super(Dog,self).__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beable', 'Mutt'])

    def fetch(self,thing):
        print '{0} goes after the {1}!' % (self.name,thing)

d = Dog('dogname')

print(d.name)
print(d.breed)
