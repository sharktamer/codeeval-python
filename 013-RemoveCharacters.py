#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    s, c = line.split(', ')
    out = ''.join(i for i in s if i not in c)
    print(out)
