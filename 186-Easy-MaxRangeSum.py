#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    n, d = line.split(';')
    n, d = int(n), [int(i) for i in d.split()]
    off = range(0, len(d) - n + 1)
    periods = [d[i:i+n] for i in off]
    max_gain = max(sum(period) for period in periods)
    out = max_gain if max_gain > 0 else 0
    print(out)
