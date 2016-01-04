#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

vals = {'Vampires': 3, 'Zombies': 4, 'Witches': 5}

for line in lines:
    d = {k: int(v) for k, v in [i.split(': ') for i in line.split(', ')]}
    candies = sum(d[i]*vals[i] for i in d if i != 'Houses') * d['Houses']
    count = sum(d[i] for i in ('Zombies', 'Vampires', 'Witches'))
    out = candies // count
    print(out)
