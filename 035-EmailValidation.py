#!/usr/bin/env python

import sys
import re

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

reg = r'^[\w\.]+\@[\w\.]+[^\.]$'

for line in lines:
    out = str(bool(re.match(reg, line))).lower()
    print(out)
