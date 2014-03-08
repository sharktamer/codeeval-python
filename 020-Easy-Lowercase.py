#!/bin/env python
import sys

with open(sys.argv[1]) as f:
    fl = f.readlines()

for l in fl:
    print l.lower(),
