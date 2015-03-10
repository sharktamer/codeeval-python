#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
    for line in f:
        a, b = line.split('|')
        print "".join([a[int(i)-1] for i in b.split()])
