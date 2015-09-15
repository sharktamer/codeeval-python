#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for i in sorted(lines[1:], key=len, reverse=True)[0:int(lines[0])]:
    print(i)
