#!/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    pairs = zip(line.split()[::2], line.split()[1::2])
    binary = ''.join(seq if flag == '0' else '1'*len(seq)
                     for flag, seq in pairs)
    print(int(binary, 2))
