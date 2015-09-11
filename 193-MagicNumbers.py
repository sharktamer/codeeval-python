#!/usr/bin/env python

import sys
from itertools import cycle


def isMagic(n):
    n = str(n)
    if '0' in n:
        return False
    c = cycle(n)
    l = []
    step = int(next(c))
    for i in range(len(n)):
        l.append(step)
        step = int([next(c) for i in range(step)][-1])
    if step != l[0] or len(set(l)) != len(n):
        return False
    return True

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    a, b = (int(i) for i in line.split())
    nums = [i for i in range(a, b+1) if isMagic(i)]
    if len(nums):
        print(' '.join(str(i) for i in nums))
    else:
        print('-1')
