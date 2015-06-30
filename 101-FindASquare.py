#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    points = sorted(eval(line))
    side_points = ((2, 0, 0, 0), (3, 1, 2, 1), (3, 0, 1, 0), (1, 1, 0, 1))
    u_sides = {points[a][b] - points[c][d] for a, b, c, d in side_points}
    out = ('false', 'true')[len(u_sides) == 1]
    print(out)
