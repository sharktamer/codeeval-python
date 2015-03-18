#!/bin/env python

import sys
from collections import Counter

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    char_counter = Counter(i for i in line.lower() if i.isalpha())
    char_counts = sorted(char_counter.values(), reverse=True)
    char_values = reversed(range(1, 27))
    out = sum(next(char_values)*i for i in char_counts)
    print(out)
