#!/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    print(int(line) == sum(pow(int(i), len(line)) for i in line))
