#!/bin/env python

import sys
import re

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    words = re.findall(r'[a-zA-Z]+', line)
    nums = re.findall(r'[0-9]+', line)
    out = '|'.join(','.join(i) for i in (words, nums) if i)
    print(out)
