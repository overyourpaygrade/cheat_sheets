#!/usr/bin/env python

def identity(f):
    return f

@identity
def foo():
    return 'bar'

print foo()
