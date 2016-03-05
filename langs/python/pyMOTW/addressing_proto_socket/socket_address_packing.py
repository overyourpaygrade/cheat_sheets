#!/usr/bin/env python

import binascii
import socket
import struct
import sys

string_address = sys.argv[1]
packed = socket.inet_aton(string_address)

print 'Original:', string_address
print 'Packed  :', binascii.hexlify(packed)
print 'Unpacked:', socket.inet_ntoa(packed)
