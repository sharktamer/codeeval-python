#!/usr/bin/env python
import sys

with open(sys.argv[1]) as f:
    fl = f.readlines()

for l in fl:
    n, p1, p2 = (int(i) for i in l.split(","))
    if bin(n)[0 - p1] == bin(n)[0 - p2]:
        print "true"
    else:
        print "false"
