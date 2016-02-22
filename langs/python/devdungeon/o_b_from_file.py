#!/usr/bin/env python3

# Reading Bytes From a File
with open('test_file.dat', 'rb') as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    print(data)

    # Seek positions and read N bytes
    binary_file.seek(0) # Go to the beggining
    couple_bytes = bynary_file.read(2)
    print(couple_bytes)

