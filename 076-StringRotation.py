#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    s1, s2 = line.split(',')
    out = any(s2[i:] + s2[:i] == s1 for i in range(len(s1)))
    print(out)
