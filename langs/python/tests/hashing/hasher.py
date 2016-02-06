#!/usr/bin/env python

import hashlib
import argparse

BLOCKSIZE = 65536
hasher_md5 = hashlib.md5()
hasher_sha1 = hashlib.sha1()

parser = argparse.ArgumentParser(description='hey')
parser.add_argument('-file', dest='afile', help='Please choose a file')
args = parser.parse_args()

if not args.afile:
    parser.print_help()
    exit(1)

with open(args.afile, 'rb') as f:

    buf = f.read(BLOCKSIZE)

    while len(buf) > 0:

        hasher_md5.update(buf)
        hasher_sha1.update(buf)

        buf = f.read(BLOCKSIZE)


print("MD5  {}".format(hasher_md5.hexdigest()))
print("SHA1 {}".format(hasher_sha1.hexdigest()))
