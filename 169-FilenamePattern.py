#!/usr/bin/env python

import sys
from fnmatch import fnmatch

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    pattern, filenames = line.split()[0], line.split()[1:]
    results = [i for i in filenames if fnmatch(i, pattern)]
    if len(results):
        print(' '.join(results))
    else:
        print('-')
