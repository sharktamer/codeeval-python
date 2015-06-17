#!/usr/bin/env python

import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    for n in (1,2):
        for i in combinations((1,2), n):
            out = [''.join(line[i:j]) for i, j in zip((0,) + i, i + (None,))]
            print(out)
