#!/usr/bin/env python

import sys
from itertools import islice

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    zeroes = line.split()
    pairs = zip(islice(zeroes, 0, None, 2), islice(zeroes, 1, None, 2))
    binary = ''.join(seq if flag == '0' else '1'*len(seq)
                     for flag, seq in pairs)
    print(int(binary, 2))
