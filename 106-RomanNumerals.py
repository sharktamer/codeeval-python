#!/usr/bin/python

import sys


def romanMe(n, s=''):
    digits = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    numerals = ('M', 'CM', 'D', 'CD', 'C',
                'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    for digit, numeral in zip(digits, numerals):
        if n >= digit:
            return romanMe(n-digit, s+numeral)
    return s

with open(sys.argv[1]) as f:
    for line in f:
        n = int(line.strip())
        print romanMe(n)
