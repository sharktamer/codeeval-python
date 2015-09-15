#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    l, out_l = [1], [1]
    for i in range(int(line.strip()) - 1):
        l = [1] + [sum(l[i:i+2]) for i in range(len(l))]
        out_l += l
    out = ' '.join(str(i) for i in out_l)
    print(out)
