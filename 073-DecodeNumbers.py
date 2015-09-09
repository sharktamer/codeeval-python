#!/usr/bin/env python

import sys


def fib():
    a, b = 1, 1
    while True:
        a, b = b, a+b
        yield a

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    f = fib()
    fibind = [next(f) for _ in range(len(line))][-1]
    out = fibind - len([i for i in line[:-1] if i not in ('1', '2')])
    print(out)
