#!/usr/bin/env python

import sys
from itertools import cycle

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    c = cycle([str.upper, str.lower])
    out = ''.join(next(c)(i) if i.isalpha() else i for i in line)
    print(out)
