#!/usr/bin/env python

import socket

print socket.gethostname()

for host in ['homer', 'www', 'www.python.org', 'nosuchname']:
    try:
        print '%15s : %s' % (host, socket.gethostbyname(host))
    except socket.error, msg:
        print '%15s : ERROR: %s' % (host, msg)
