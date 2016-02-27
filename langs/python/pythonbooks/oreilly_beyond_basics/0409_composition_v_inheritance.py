#!/usr/bin/env python

import random
import StringIO

class WriteMyStuff(object):

    def __init__(self, writer):
        self.writer = writer

    def write(self):
        write_text = "this is a silly message"
        self.writer.write(write_text)

fh = open('0409_test.txt', 'w')
w1 = WriteMyStuff(fh)
w1.write()
fh.close()

sioh = StringIO.StringIO()
w2 = WriteMyStuff(sioh)
w2.write()

print 'file object:  ', open('0409_test.txt','r').read()
print 'StringIO object:  ', sioh.getvalue()

