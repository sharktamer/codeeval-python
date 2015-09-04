#!/usr/bin/env python

import sys
import re
from itertools import permutations

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    wines, letters = line.split(' | ')
    wines = wines.split()
    found = [j for j in wines if
             any(re.search('.*?'.join(i), j) for i in permutations(letters))]
    if found:
        out = ' '.join(found)
    else:
        out = 'False'
    print(out)
