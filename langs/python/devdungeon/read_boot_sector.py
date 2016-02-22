#!/usr/bin/env python3

import sys

in_file = open(sys.argv[1], 'rb') # Provide a path to disk or ISO
chunk_size = 512
data = in_file.read(chunk_size)
print(data)
