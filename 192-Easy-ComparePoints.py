#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

ordinate_list = [
    []
]

for line in lines:
    o, p, q, r = [int(i) for i in line.split()]
    x = (('E', 'W')[o-q > 0], '')[not o-q]
    y = (('N', 'S')[p-r > 0], '')[not p-r]
    if y+x:
        print(y+x)
    else:
        print('here')
