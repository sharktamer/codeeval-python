#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    split = [i.split() for i in line.split('|')]
    cols = zip(*split)
    maxes = [max(int(j) for j in i) for i in cols]
    out = ' '.join(str(i) for i in maxes)
    print(out)
