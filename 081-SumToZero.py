#!/usr/bin/env python

import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    nums = map(int, line.split(','))
    out = len([i for i in combinations(nums, 4) if sum(i) == 0])
    print(out)
