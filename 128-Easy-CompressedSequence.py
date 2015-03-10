#!/usr/bin/env python

import sys
from itertools import groupby, chain

with open(sys.argv[1]) as f:
    for line in f:
        ls = line.split()
        outlist = [(str(len(list(g))), k) for k, g in groupby(ls)]
        out = ' '.join(list(chain(*outlist)))
        print(out)

