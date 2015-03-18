#!/usr/bin/env python

import sys
from datetime import datetime

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    t1, t2 = [datetime.strptime(i, '%H:%M:%S') for i in line.split()]
    diff = max(t1-t2, t2-t1, key=lambda x: x.days).seconds
    hours = diff // 3600
    minutes = (diff % 3600) // 60
    seconds = (diff % 3600) % 60
    out = '{0:02d}:{1:02d}:{2:02d}'.format(hours, minutes, seconds)
    print(out)
