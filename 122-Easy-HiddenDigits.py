#!/usr/bin/python

import sys
import re
import string

m = string.maketrans('abcdefghij', '0123456789')

with open(sys.argv[1]) as f:
    for line in f:
        trans = line.strip().translate(m)
        out = "".join(re.findall(r'\d', trans))
        if len(out) == 0:
            print('NONE')
        else:
            print(out)
