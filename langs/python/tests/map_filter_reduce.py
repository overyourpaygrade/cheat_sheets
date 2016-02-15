#!/usr/bin/env python

def square(number):
    return number * number

def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def sum(x,y):
    return x + y

numbers =[1,2,3]
print("\nSquare numbers in a list")
print(numbers)
numberssq = list(map(square, numbers))
print(numberssq), "\n"

numbers_one = list(range(1,11))
print("Print only even numbers")
print(numbers_one)
evens = list(filter(even, numbers_one))
print(evens), "\n"

import functools
print("Take the range a sum all the numbers")
print(numbers_one)
sum = functools.reduce(sum, numbers_one)
print("The sum of the range is " + str(sum)), "\n"
