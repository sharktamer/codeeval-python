#!/bin/env python

import sys
import csv

with open(sys.argv[1]) as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print ",".join(sorted(set(row)))
