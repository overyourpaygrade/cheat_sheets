#!/usr/bin/env python

import subprocess

out_bytes = subprocess.check_output(['netstat','-a'])
out_text = out_bytes.decode('utf-8')

try:
    out_bytes = subprocess.check_output(['ls', '-l', '-a'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output
    code = e.returncode

# With stdout
out_bytes = subprocess.check_output(['ls','-l','-a'],
                                    stderr=subprocess.STDOUT)

# With a timeout
try:
    out_bytes = subprocess.check_output(['ls','-l','-a'], timeout=5)
except subprocess.TimeoutExpired as e:
    out_bytes = e.output
    code = e.returncode

# Interpreted by a shell
out_bytes = subprocess.check_output('grep python | wc > out', shell=True)
