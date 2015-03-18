#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
    for line in f:
        n, e = line.split()
        ec = e.replace('+', '').replace('-', '')
        t = str.maketrans(ec, n)
        print(eval(e.translate(t)))
