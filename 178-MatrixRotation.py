#!/bin/env python

import sys
from math import sqrt

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    elements = line.split()
    n = int(sqrt(len(elements)))
    # One liner version of itertools grouper example
    matrix = list(zip(*[iter(elements)]*n))
    rotated = zip(*matrix[::-1])
    out = ' '.join(' '.join(i for i in j) for j in rotated)
    print(out)
