#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    ls = line.split()
    n = int(ls[0])
    digits = map(int, ls[1].split(','))
    if len([i for i in zip(*[iter(digits)]*n) if len(set(i)) == n]) == n:
        print('True')
    else:
        print('False')
