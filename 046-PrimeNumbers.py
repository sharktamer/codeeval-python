#!/usr/bin/env python

import sys


def isPrime(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    n = int(line)
    out = ','.join(str(i) for i in range(2, n) if isPrime(i))
    print(out)
