#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()


def dub(x):
    return x*2 // 10 + x*2 % 10

for line in lines:
    procline = line.replace(' ', '')[::-1]
    s1 = [int(j) if i % 2 else dub(int(j)) for i, j in enumerate(procline, 1)]
    out = (0, 1)[not sum(s1) % 10]
    print(out)
