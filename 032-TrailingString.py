#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    s1, s2 = line.split(',')
    out = int(s1.endswith(s2))
    print(out)
