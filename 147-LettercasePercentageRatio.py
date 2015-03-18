#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    lower = len([i for i in line if i.islower()]) / len(line) * 100
    upper = len([i for i in line if i.isupper()]) / len(line) * 100
    out = 'lowercase: {0:.2f} uppercase: {1:.2f}'.format(lower, upper)
    print(out)
