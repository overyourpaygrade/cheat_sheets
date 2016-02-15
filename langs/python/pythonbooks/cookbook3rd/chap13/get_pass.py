#!/usr/bin/env python3

import getpass

user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user,passwd):
    print('Yay!')
else:
    print('Boo!')

