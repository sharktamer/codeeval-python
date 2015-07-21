#!/usr/bin/env python

import sys
import re

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    out = re.sub(r'[^A-Za-z]+', ' ', line).strip().lower()
    print(out)
