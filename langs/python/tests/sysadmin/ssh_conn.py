#!/usr/bin/env python

from pexpect import pxssh

host_ip = ""
host_un = ""
host_pw = ""
p = pxssh.pxssh()

try:
    p.login(host_ip,host_un,host_pw)
except:
    raise

p.sendline('ls -l')
p.expect('#')

req1 = p.before

p.sendline('uptime')
p.expect('#')

req2 = p.before

p.logout()

print req1
print req2
