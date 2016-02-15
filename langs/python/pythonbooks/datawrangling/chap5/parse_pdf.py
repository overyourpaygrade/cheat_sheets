#!/usr/bin/env python

import slate

pdf = 'NeXpose_Install.pdf'

with open(pdf) as f:
    doc = slate.PDF(f)

for page in doc[:2]:
    print page

with open(pdf) as f:
    for line in f:
        print line
