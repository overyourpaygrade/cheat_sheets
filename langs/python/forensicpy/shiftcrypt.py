#!/usr/bin/env python
#https://github.com/pcchou/ctf-writeups/tree/master/ekoparty-2015/cry200

import struct
import sys
import base64

#if len(sys.argv) != 2:
#    print "Usage: %s data" % sys.argv[0]
#    exit(0)

data = sys.argv[1]
#data = base64.b64decode("CjBPewYGc2gdD3RpMRNfdDcQX3UGGmhpBxZhYhFlfQA=")

# With a block size of 4 chars, pad the final block with \x00
padding = 4 - len(data) % 4
if padding != 0:
    data = data + "\x00" * padding

# Store in a tuple the data. 
# Format: unsigned integer * len data / 4
result = []
blocks = struct.unpack("I" * (len(data) / 4), data)

# For each block of data XOR with the same SHR 16
for block in blocks:
    result += [block ^ block >> 16]

# Pack it all in and store in output as str
output = ''
for block in result:
    output += struct.pack("I", block)

# Encode the otput as base64
print base64.b64encode(output)
#print output

