#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    bugs = sum(not(i == j) for i, j in zip(*line.split(' | ')))
    if bugs > 6:
        print('Critical')
    elif bugs > 4:
        print('High')
    elif bugs > 2:
        print('Medium')
    elif bugs > 0:
        print('Low')
    else:
        print('Done')
