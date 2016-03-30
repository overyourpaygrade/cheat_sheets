#!/usr/bin/env python

import re

line='<City_State>PLAINSBORO, NJ 08536-1906</City_State>'

print re.match('>.*<', line)

print re.search('>.*<', line)

print re.search('>.*<', line).group(0)

print re.search('>.*<', line).group()
