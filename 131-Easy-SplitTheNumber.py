#!/usr/bin/python

import sys
# import re

# with open(sys.argv[1]) as f:
#     for line in f:
#         n, e = line.split()
#         p = re.search('[\+\-]', e).start()
#         print eval(n[:p] + e[p] + n[p:])

from string import maketrans

with open(sys.argv[1]) as f:
    for line in f:
        n, e = line.split()
        ec = e.replace('+', '').replace('-', '')
        t = maketrans(ec, n)
        print(eval(e.translate(t)))
