#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    # Split line into two 4 element lists (overly fancy)
    rec1, rec2 = zip(*[iter(int(i) for i in line.split(','))]*4)
    # print(rec1, rec2)
