#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    l, k = line.split(';')
    l = l.split(',')
    k = int(k)

    # Reverse as many elements as able
    r = [','.join(i[::-1]) for i in zip(*[iter(l)]*k)]
    # Get the remainder if the number of elements is not a multiple of k
    if len(l) % k:
        rem = l[-(len(l) % k):]
    else:
        rem = []
    out = ','.join(str(i) for i in r + rem)
    print(out)
