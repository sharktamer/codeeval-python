#!/usr/bin/python

import sys
from collections import Counter

with open(sys.argv[1]) as f:
    for line in f:
        e = line.split(',')
        c = Counter(e)
        value, count = c.most_common()[0]
        if count >= len(e) / 2:
            print(value)
        else:
            print(None)
