#!/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    l, swaps = line.split(' : ')
    l, swaps = l.split(), swaps.split(', ')
    for s in swaps:
        s1, s2 = [int(i) for i in s.split('-')]
        l[s1], l[s2] = l[s2], l[s1]
    out = ' '.join(l)
    print(out)
