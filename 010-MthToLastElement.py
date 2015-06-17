#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    series, n = line.split()[:-1], int(line.split()[-1])
    if n <= len(series):
        out = series[0-n]
        print(out)
