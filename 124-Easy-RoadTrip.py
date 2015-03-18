#!/usr/bin/env python

import sys
from itertools import islice

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    distances = [0] + [int(i.split(',')[1]) for i in line.split(';') if i]
    distances.sort()
    out = [d2 - d1 for d1, d2 in zip(distances, islice(distances, 1, None))]
    print(','.join(str(i) for i in out))
