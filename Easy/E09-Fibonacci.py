#!/bin/env python
import sys


with open(sys.argv[1]) as f:
    fl = f.readlines()

for l in fl:
    fib = [0, 1]
    for i in range(int(l)-1):
        fib.append(fib[-1] + fib[-2])
    print fib[int(l)]
