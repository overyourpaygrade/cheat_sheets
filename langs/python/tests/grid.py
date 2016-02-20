#!/usr/bin/env python

import math

x = "156/56"
xr = 20
x1 = 56
y1 = 156

y = "160/59"
yr = 40
x2 = 59
y2 = 160

# Add 3' top or bottom
# If 1-14, 15-28, 29-42
# add 3 6 9 or 2 4 6
# Depending on the direction
# 73 inches tall ~6'

print abs(( x2-x1 )) + abs(( y2-y1 ))
