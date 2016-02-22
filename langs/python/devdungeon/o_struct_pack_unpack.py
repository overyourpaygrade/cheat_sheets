#!/usr/bin/env python3

import struct

# Packing values to bytes
# The first parameter is the format string. Here it specifies 
# the data is structured with a single four-byte integer followed
# by two characters.
# The rest of the parameters are the values for each item in order
binary_data = struct('icc', 8499000, b'A', b'Z')
print(binary_data)

# When unpacking, you recieve a tuple of all data in the same order
tuple_of_data = struct('icc', binary_data)
print(tuple_of_data)

# For more information on format strings and endiannes, refer to
# http://docs.python.org/3.5/library/struct.html
