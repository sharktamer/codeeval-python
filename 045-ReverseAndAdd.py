#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    n, c = int(line), 0
    while str(n) != str(n)[::-1]:
        n += int(str(n)[::-1])
        c += 1
    print(c, n)
