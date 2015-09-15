#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

d = {'0': '1', '1': '2', '2': '0'}
seq = '0'
seq_len = max(int(i) for i in lines)
while len(seq) < seq_len:
    seq += ''.join(d[i] for i in seq)

for line in lines:
    print(seq[int(line)])
