#!/usr/bin/env python

import sys
from itertools import groupby

rotations = {
    'LEFT': 0,
    'DOWN': 1,
    'RIGHT': 2,
    'UP': 3
}

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    # split line into variables
    direction, length, grid = [i.strip() for i in line.split(';')]
    grid = [[int(j) for j in i.split()] for i in grid.split('|')]
    # rotate grid to allow left movement
    for i in range(rotations[direction]):
        grid = list(zip(*grid[::-1]))
    # shift rows to left
    grid = [sorted(i, key=lambda x: x == 0) for i in grid]
    # merge shifted cells
    grid = [[sum(j[1]) for j in groupby(i)] for i in grid]
    grid = [i + [0] * (int(length)-len(i)) for i in grid]
    # rotate grid back to initial position
    for i in range(4 - rotations[direction]):
        grid = list(zip(*grid[::-1]))
    print('|'.join(' '.join(map(str, i)) for i in grid))
