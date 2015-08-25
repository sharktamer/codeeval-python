#!/usr/bin/env python

import sys
from collections import Counter

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    if line:
        a = [int(i) for i in line.split(';')[1].split(',')]
        c = Counter(a)
        dup = [i for i in c if c[i] > 1][0]
        print(dup)
