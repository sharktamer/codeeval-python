#!/bin/env python

import sys

with open(sys.argv[1]) as f:
    for line in f:
        print(int(not int(line) % 2))

