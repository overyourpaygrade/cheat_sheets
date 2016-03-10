#!/usr/bin/env python

import time

def tail(filename):

    with open(filename, 'r') as f:

        f.seek(0,2)
        try:
            while True:
                where = f.tell()
                line = f.readline()

                if not line:
                    time.sleep(0.1)
                    f.seek(where)
                else:
                    print line.rstrip()

        except KeyboardInterrupt:

            exit(1)

file_loc = 'test2.txt'

tail(file_loc)

