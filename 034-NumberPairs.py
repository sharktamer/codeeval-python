#!/usr/bin/env python

import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    nums, goal = line.split(';')
    nums = [int(i) for i in nums.split(',')]
    goal = int(goal)
    combos = [i for i in combinations(nums, 2) if sum(i) == goal]
    if len(combos) == 0:
        out = 'NULL'
    else:
        out = ';'.join(','.join(str(j) for j in i) for i in combos)
    print(out)
