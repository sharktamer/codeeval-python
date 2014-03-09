#!/usr/bin/python

import sys
import re

with open(sys.argv[1]) as f:
    for line in f:
        n, e = line.split()
        p = re.search('[\+\-]', e).start()
        print eval(n[:p] + e[p] + n[p:])
