#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    names, (num,) = [i.split() for i in line.split(' | ')]
    num = int(num)
    while len(names):
        out = names.pop(num % len(names)-1)
    print(out)
