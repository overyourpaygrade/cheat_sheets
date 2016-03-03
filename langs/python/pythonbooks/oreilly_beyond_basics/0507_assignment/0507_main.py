#!/usr/bin/env python

from assignment3 import ConfigDict

cc = ConfigDict('0507_config_file.txt')

print(cc['sql_query'])
print(cc['email_to'])

cc['database'] = 'mysql_managed'

print cc
