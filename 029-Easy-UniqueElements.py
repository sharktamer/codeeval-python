#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    for line in f:
        ints = [int(i) for i in line.split(',')]
        s = sorted(set(ints))
        out = ','.join([str(i) for i in s])
        print out
