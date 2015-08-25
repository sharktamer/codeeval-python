#!/usr/bin/env python

import sys
from operator import add, sub, mul, truediv
from itertools import product, permutations


def getExp(ol, nl):
    return ol[0](ol[1](ol[2](ol[3](nl[0], nl[1]), nl[2]), nl[3]), nl[4])

ops = (add, sub, mul, truediv)

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    nums = [int(i) for i in line.split()]
    solutions = [1 for o, n
                 in product(permutations(ops*4, 4), permutations(nums))
                 if getExp(o, n) == 42]
    if len(solutions):
        print('YES')
    else:
        print('NO')
