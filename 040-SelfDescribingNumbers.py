#!/usr/bin/python

import sys


def selfDescribing(number):
    for n, d in enumerate(number):
        if int(d) != len(filter(lambda x: x == str(n), number)):
            return 0
    return 1


with open(sys.argv[1]) as f:
    for line in f:
        print selfDescribing(line.strip())
