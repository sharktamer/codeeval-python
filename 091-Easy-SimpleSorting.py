#!/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    nums = [float(i) for i in line.split()]
    nums.sort()
    out = ' '.join('{0:.3f}'.format(i) for i in nums)
    print(out)
