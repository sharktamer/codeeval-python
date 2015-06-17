#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    word, code = line.split()
    out = ''.join(c.upper() if int(d) else c for c, d in zip(word, code))
    print(out)
