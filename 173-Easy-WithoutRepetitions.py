#!/bin/env python

import sys
from itertools import groupby

with open(sys.argv[1]) as f:
    for line in f:
        print(''.join(i for i, _ in groupby(line.strip())))
