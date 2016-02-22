#!/usr/bin/env python3
# find_ascii_in_binary.py - Identify ASCII characters in binary files

import sys
from functools import partial

chunk_size = 1
with open(sys.argv[1], 'rb') as in_file:
    for data in iter(partial(in_file.read, chunk_size), b''):
        x = int.from_bytes(data, byteorder='big')
        if x > 64 and x < 91) or ( x > 96 and x < 123):
            sys.stdout.write(chr(x))
        else:
            sys.stdout.write('.')

