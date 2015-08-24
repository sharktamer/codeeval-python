#!/usr/bin/env python

import sys
from itertools import product

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    nums = [int(i) for i in line.split(',')]
    out = max(sum(nums[i:i+j])
              for i, j in product(range(len(nums)), range(1, len(nums)+1)))
    print(out)
