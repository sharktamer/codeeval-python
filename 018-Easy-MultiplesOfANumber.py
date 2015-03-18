#!/usr/bin/env python
import sys

in_file = sys.argv[1]
with open(in_file) as f:
    fl = f.readlines()

for l in fl:
    x, n = (int(i) for i in l.split(","))
    out = 0
    i = 1
    while out < x:
        out = n * i
        i += 1
    print(out)
