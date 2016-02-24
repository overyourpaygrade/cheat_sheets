#!/usr/bin/env python3

import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

# Create a file
size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

# Map the data into memory?
m = memory_map('data')
print(len(m))

# Print a segment of that dataset
print(repr(m[0:10]))

# Re-assign a slice
m[0:11] = b'Hello World'
m.close()

# Changes to the file
with open('data', 'rb') as f:
    print()
    print(f.read(11))

# Verify Changes
with memory_map('data') as m:
    print()
    print(len(m))
    print(m[0:11])
    m.closed

