#!/bin/env python
import sys

in_file = sys.argv[1]
with open(in_file) as f:
    fs = f.readlines()

for l in fs:
    f, b, n = (int(i) for i in l.split())
    out_list = []
    for i in range(1, n + 1):
        out_list.append(((i, "B"), ("F", "FB"))[i % f == 0][i % b == 0])
    print " ".join(str(i) for i in out_list)
