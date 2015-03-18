#!/usr/bin/env python
import sys

in_file = sys.argv[1]
with open(in_file) as f:
    file = f.readlines()

for l in file:
    print(" ".join(l.split()[::-1]))
