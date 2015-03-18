#!/usr/bin/python

import sys


def romanMe(n, s=''):
    numerals = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
                (5, 'V'), (4, 'IV'), (1, 'I'))
    for digit, numeral in numerals:
        if n >= digit:
            return romanMe(n - digit, s + numeral)
    return s

with open(sys.argv[1]) as f:
    for line in f:
        n = int(line.strip())
        print(romanMe(n))
