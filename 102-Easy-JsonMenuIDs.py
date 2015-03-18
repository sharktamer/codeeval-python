#!/usr/bin/env python

import sys
import re

r = re.compile(r'"Label (.*?)"')

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()
lines = [i for i in lines if i]

for line in lines:
    out = sum(int(i) for i in r.findall(line) if line.strip())
    print(out)
