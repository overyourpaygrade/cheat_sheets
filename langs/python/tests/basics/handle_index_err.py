#!/usr/bin/env python

with open('w_pid.txt', 'rb') as f:

    for line in f:
        fh = line.split(' ')

        dct = {
            'Name': fh[4],
            'Something': fh[5],
            'PID': fh[6],
            'Status': fh[7],
            }

with open('pid_missing.txt', 'rb') as f:

    for line in f:
        fh = line.split(' ')

        # Create the dictionary
        dct = {
            'Name': fh[4],
            'Something': fh[5],
            }

        # Handle the exception and re-order the assignment
        try:
            # If the len is 8 all good
            dct['PID'] = fh[6]
            dct['Status'] = fh[7].rstrip()
        except IndexError:
            # If the len is 7 then swap
            dct['PID'] = None
            dct['Status'] = fh[6].rstrip()

        print dct

