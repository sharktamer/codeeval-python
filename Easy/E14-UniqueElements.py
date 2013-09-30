#!/bin/env python

import sys

# sum = 0
with open(sys.argv[1]) as f:
    for l in f.readlines():
        print ",".join(sorted(set([i.strip() for i in l.split(",")])))
