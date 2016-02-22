#!/usr/bin/env python3

# Some bytes to play with
byte1 = int('11110000', 2) # 240
byte2 = int('00001111', 2) # 15
byte3 = int('01010101', 2) # 85

print('Ones complement (flip the bits)')
print(~byte1)

print('AND')
'''
a	b	a AND b
0	0	0
0	1	0
1	0	0
1	1	1
'''
print(byte1 & byte2)

print('OR')
'''
a	b	a OR b
0	0	0
0	1	1
1	0	1
1	1	1
'''
print(byte1 | byte2)

print('XOR')
'''
a	b	a XOR b
0	0	0
0	1	1
1	0	1
1	1	0
'''
print(byte1 ^ byte2)

print('SHR - Shifting right will lose the right-most bits')
print(byte2 >> 3)

print('SHL - Shifting left will add a 0 bit on the right side')
print(byte2 << 1)

print('See if a single bit is set')
bit_mask = int('00000001', 2) # Bit 1
print(bit_mask & byte1) # Is bit set in byte1?
print(bit_mask & byte1) # Is bit set in byte2?
