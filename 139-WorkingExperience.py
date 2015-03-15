#!/bin/env python

import sys
from datetime import datetime

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    date_periods = [
        [datetime.strptime(d, '%b %Y') for d in i.split('-')]
        for i in line.split('; ')
    ]

# Sort list in order of start date
# date_periods.sort(key=lambda x: x[0])

# Gets a list of elements n and n+1 for comparison
# from itertools import islice
# zip(date_periods, islice(date_periods, 1, None))
