#!/usr/bin/env python

import sys

mprimes = [3, 7, 31, 127, 2047]

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    limit = int(line.strip())

    out = ', '.join(str(i) for i in mprimes if i < limit)

    print(out)
