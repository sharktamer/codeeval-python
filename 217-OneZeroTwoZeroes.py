#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    zeroes, end = [int(i) for i in line.split()]
    bins = [format(i, 'b') for i in range(1, end+1)]
    matches = [i for i in bins if i.count('0') == zeroes]
    out = len(matches)
    print(out)
