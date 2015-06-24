#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    ls = line.split()
    n = int(ls[0])
    goes = ls[1:-1]
    hilow = {
        'Lower': lambda x: x[:len(x)//2],
        'Higher': lambda x: x[len(x)//2+1:]
    }
    r = range(n)
    for i in goes:
        r = hilow[i](r)
    print(r[len(r)//2])
