#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    word = max(line.split(), key=lambda x: len(x))
    out = ' '.join('*'*int(n) + i for n, i in enumerate(word))
    print(out)
