#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    door_count, iterations = (int(i) for i in line.split())
    doors = [False for i in range(door_count)]
    for _ in range(iterations-1):
        doors = [i if n % 2 else not i for n, i in enumerate(doors, 1)]
        doors = [i if n % 3 else not i for n, i in enumerate(doors, 1)]
    doors[-1] = not doors[-1]
    out = len([i for i in doors if i is False])
    print(out)
