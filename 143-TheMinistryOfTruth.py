#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    u1, u2 = line.split(';')
    u1 = ' '.join(u1.split())
    u2l = list(u2)
    out = ''.join(u2l.pop(0) if len(u2l) and i == u2l[0] else '_' for i in u1)
    if len(u2l):
        print('I cannot fix history')
    else:
        print(out)
