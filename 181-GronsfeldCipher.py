#!/usr/bin/env python

import sys
from itertools import cycle

ab = (' !"#$%&\'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk'
      'lmnopqrstuvwxyz')

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    key, em = line.split(';')
    c = cycle(key)
    out = ''.join(ab[ab.index(i)-int(next(c))] for i in em)
    print(out)
