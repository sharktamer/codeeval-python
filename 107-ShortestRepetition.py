#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
    for line in f:
        l = line.strip()
        print len((l.split(l[0]))[1]) + 1
