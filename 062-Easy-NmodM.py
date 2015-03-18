#!/usr/bin/env python

import sys
from itertools import count

def myMod(x, y):
    for i in count(0, y):
        if i > a:
            return a - (i - b)

with open(sys.argv[1]) as f:
    for line in f:
        a, b = map(int, line.split(','))
        print(myMod(a, b))

