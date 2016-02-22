#!/usr/bin/env python3

# Text Encoding
# Binary to text
binary_data = b'I am text.'
text = binary_data.decode('utf-8')
print(text)

binary_data = bytes([65, 66, 67]) # ASCII values for A, B, C
text = binary_data.decode('utf-8')
print(text)

# Text to Binary
message = 'Hello' # str
binary_message = message.encode('utf-8')
print(type(binary_message)) # bytes

# Python has many built in encodings for different languages
# and even the Caesar cipher is built in
import codecs
cipher_text = codecs.encode(message, 'rot_13')
print(cipher_text)

