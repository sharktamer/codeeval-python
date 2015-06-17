#!/usr/bin/env python

import sys


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    n1, n2 = map(int, line.split(','))
    out = len([i for i in range(n1, n2+1) if isPrime(i)])
    print(out)
