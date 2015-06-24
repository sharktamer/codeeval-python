#!/usr/bin/env python

import sys
import re
from math import sqrt


def hyp(x, y):
    return sqrt(x**2 + y**2)

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    c1, c2, r, p1, p2 = map(float, re.findall(r'\d+\.?\d*', line))
    dist = hyp(abs(c1-p1), abs(c2-p2))
    out = ('true', 'false')[r <= dist]
    print(out)
