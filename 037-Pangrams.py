#!/usr/bin/env python

import sys
from string import ascii_lowercase

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    out = ''.join(i for i in ascii_lowercase if i not in line.lower())
    print(out or 'NULL')
