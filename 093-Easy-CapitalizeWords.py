#!/bin/env python

import sys
from string import capwords

with open(sys.argv[1]) as f:
    for line in f:
        print(' '.join([i[0].upper() + i[1:] for i in line.split()]))

