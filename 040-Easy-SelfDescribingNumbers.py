#!/usr/bin/python

import sys


def selfDescribing(number):
    for n, d in enumerate(number):
        if int(d) != len([i for i in number if i == str(n)]):
            return 0
    return 1

with open(sys.argv[1]) as f:
    for line in f:
        print(selfDescribing(line.strip()))
