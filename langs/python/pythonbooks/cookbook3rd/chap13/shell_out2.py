#!/usr/bin/env python

import subprocess

# Some test to send
text = b'''
hello word
this is a test
goodbye
'''

# Launch a command with pipes
p = subprocess.Popen(['wc'],
            stdout = subprocess.PIPE,
            stdin = subprocess.PIPE)

# Send the data and get the output
stdout, stderr = p.communicate(text)

# To interpret as text, decode
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')
