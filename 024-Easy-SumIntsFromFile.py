#!/bin/env python
import sys

# sum = 0
with open(sys.argv[1]) as f:
    print sum([int(l) for l in f.readlines()])
