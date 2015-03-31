#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    houses = [int(i) for i in line.split()][1:]
    out = min(sum(abs(i-j) for j in houses) for i in range(1, max(houses)))
    print(out)
