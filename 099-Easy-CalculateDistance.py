#!/bin/env python

import sys
import re
from math import sqrt

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    x1, y1, x2, y2 = [int(i) for i in re.findall(r'-?[0-9]+', line)]
    a, b = (x1-x2), (y1-y2)
    out = int(sqrt(a**2 + b**2))
    print(out)
