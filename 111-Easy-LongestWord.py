#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
    for line in f:
        print(max(line.split(), key=len))
