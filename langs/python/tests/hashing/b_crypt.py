#!/usr/bin/env python

import bcrypt

password = b"super secret password"

# Hash a password for the first time, with a random salt

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Check that an unhahsed password matches one that has been 
# previously hashed

if bcrypt.hashpw(password, hashed) == hashed:
	print("It matches!")
else:
	print("It does not match :(")

print hashed
