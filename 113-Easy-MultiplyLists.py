#!/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    pairs = zip(*[i.split() for i in line.split('|')])
    out = ' '.join(str(int(a)*int(b)) for a, b in pairs)
    print(out)
