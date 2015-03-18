#!/bin/env python

import sys

with open(sys.argv[1]) as f:
    for line in f:
        s1, s2 = [set(i.split(',')) for i in line.strip().split(';')]
        out = ','.join(sorted(s1 & s2))
        print(out)
