#!/usr/bin/env python

import sys
from string import ascii_lowercase
from operator import add

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
         (2, 1), (2, -1), (-2, 1), (-2, -1)]

for line in lines:
    c, n = line
    pos = (ascii_lowercase.find(c) + 1, int(n))
    all_moves = [list(map(add, pos, i)) for i in moves]
    val_moves = [(x, y) for x, y in all_moves if 0 < x <= 8 and 0 < y <= 8]
    out = ' '.join(sorted(ascii_lowercase[x-1] + str(y) for x, y in val_moves))
    print(out)
