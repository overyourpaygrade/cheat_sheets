#!/usr/bin/env python

import struct

packed = struct.pack('>i4sh',7,b'spam',8)

print type(packed)
print list(packed)

file_ = open('data.bin', 'wb')
file_.write(packed)

file_.close()

data = open('data.bin','rb').read()

print type(data)
print list(data)

print struct.unpack('>i4sh', data)
