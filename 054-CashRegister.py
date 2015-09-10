#!/usr/bin/env python

import sys

d = {1: 'PENNY',
     5: 'NICKEL',
     10: 'DIME',
     25: 'QUARTER',
     50: 'HALF DOLLAR',
     100: 'ONE',
     200: 'TWO',
     500: 'FIVE',
     1000: 'TEN',
     2000: 'TWENTY',
     5000: 'FIFTY',
     10000: 'ONE HUNDRED'}

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    pp, ch = [int(float(i)*100) for i in line.split(';')]
    if pp > ch:
        out = 'ERROR'
    else:
        coins = []
        c = ch - pp
        while c != 0:
            for i in sorted(d)[::-1]:
                if c // i > 0:
                    coins.append(i)
                    c -= i
        if len(coins):
            out = ','.join(d[i] for i in sorted(coins)[::-1])
        else:
            out = 'ZERO'
    print(out)
