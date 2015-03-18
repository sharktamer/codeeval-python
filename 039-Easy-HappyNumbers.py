#!/usr/bin/python

import sys


def isHappy(n):
    while True:
        if n == '1':
            return 1
        elif n == '4':
            return 0
        n = str(sum([int(i)**2 for i in n]))

with open(sys.argv[1]) as f:
    for line in f:
        print(isHappy(line.strip()))
