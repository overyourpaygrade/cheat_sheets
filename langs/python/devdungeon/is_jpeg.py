#is_jpeg.py - Does the file have a JPEG binary signature?

import sys
import binascii

jpeg_signatures = [
	binascii.unhexlify(b'FFD8FFD8'),
	binascii.unhexlify(b'FFD8FFE0'),
	binascii.unhexlify(b'FFD8FFE1')
]

with open(sys.argv[1], 'rb') as file:
	first_four_bytes = file.read(4)

	if first_four_bytes in jpeg_signatures:
		print("JPEG detected.")
	else:
		print("File does not look like a JPEG")
