#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    out = ' '.join(sorted(line.split(), reverse=True))
    print(out)
