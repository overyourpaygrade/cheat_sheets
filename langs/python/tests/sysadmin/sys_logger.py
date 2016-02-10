#!/usr/bin/env python
import syslog

syslog.syslog('app: started logging')

for a in ['a', 'b', 'c']:
	b = 'app: I found letter '+a
	syslog.syslog(b)

syslog.syslog('app: the script goes night-night!')

