#!/usr/bin/env python

import re

with open('apache_sample.txt') as apache_fh:

    for line in apache_fh:

        if re.match('.*robots\.txt', line):
            print "simple re match", line.strip()

        if re.match('\S+\.com', line):
            print line.strip()

        if re.search('(\d{3})\s(\d{2,4})', line).group():
            print line
        '''
        64.242.88.10 - - [07/Mar/2004:17:53:45 -0800]
        '''

        print re.search('(\d{3})\s(\d{2,4})', line).group()
        '''200 7771'''

        match = re.search('(\d{3})\s(\d{2,4})', line)

        print "both  ", match.group()
        print "first ", match.group(1)
        print "second", match.group(2)

        '''
        both   200 7771
        first  200
        second 7771
        '''
