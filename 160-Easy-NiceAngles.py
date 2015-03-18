#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    num = float(line)
    degrees = int(num)
    minutes = int(num % 1 * 60)
    seconds = int(num % 1 * 60 % 1 * 60)
    out = '{0}.{1:02d}\'{2:02}"'.format(degrees, minutes, seconds)
    print(out)
