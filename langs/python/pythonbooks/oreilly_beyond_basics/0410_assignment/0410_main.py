#!/usr/bin/env python

from assignment import LogFile, DelimFile

log = LogFile('0410_log.txt')
c = DelimFile('0410_test.csv', ',')

log.write('this is a log message')
log.write('this is another log message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])
