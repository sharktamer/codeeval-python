#!/usr/bin/env python

import sys
import re

in_file = sys.argv[1]

with open(in_file) as f:
    for line in f:
        print(min([len(re.search(r'X(\.*)Y', i).group(1))
              for i in line.split(',')]))
