#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

arrows = ('<--<<', '>>-->')
for l in lines:
    out = len([l[n: n + 5] for n in range(len(l)) if l[n: n + 5] in arrows])
    print(out)
