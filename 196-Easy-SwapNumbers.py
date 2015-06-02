#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    out = ' '.join(i[-1] + i[1:-1] + i[0] for i in line.split())
    print(out)
