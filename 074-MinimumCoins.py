#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    count = int(line)
    out = 0
    for coin in (5, 3, 1):
        out += count//coin
        count = count-((count//coin)*coin)
    print(out)
