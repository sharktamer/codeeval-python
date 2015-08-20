#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()


def goodChain(d):
    k = d['BEGIN']
    for i in range(len(d) - 1):
        if k == 'END':
            return 'BAD'
        k = d[k]
    if k == 'END':
        return 'GOOD'
    return 'BAD'


for line in lines:
    d = dict([i.split('-') for i in line.split(';')])
    out = goodChain(d)
    print(out)
