#!/usr/bin/env python

from assignment2 import WriteFile, CSVFormatter, LogFormatter

writecsv = WriteFile('0410_text2.csv', CSVFormatter)
writelog = WriteFile('0410_log2.txt', LogFormatter)

writecsv.write(['a', 'b,2', 'c', 'd'])
writelog.write('this is a log message')

writecsv.write(['1', '2', '3', '4'])
writelog.write('this is another log message')

writecsv.close()
writelog.close()
