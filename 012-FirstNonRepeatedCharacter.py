#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    out = [i for i in line if line.count(i) == 1][0]
    print(out)
