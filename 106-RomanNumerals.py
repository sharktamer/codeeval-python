#!/usr/bin/python

import sys


def romanMe(n, s=''):
    if n >= 1000:
        return romanMe(n-1000, s+'M')
    elif n >= 900:
        return romanMe(n-900, s+'CM')
    elif n >= 500:
        return romanMe(n-500, s+'D')
    elif n >= 400:
        return romanMe(n-400, s+'CD')
    elif n >= 100:
        return romanMe(n-100, s+'C')
    elif n >= 90:
        return romanMe(n-90, s+'XC')
    elif n >= 50:
        return romanMe(n-50, s+'L')
    elif n >= 40:
        return romanMe(n-40, s+'XL')
    elif n >= 10:
        return romanMe(n-10, s+'X')
    elif n >= 9:
        return romanMe(n-9, s+'IX')
    elif n >= 5:
        return romanMe(n-5, s+'V')
    elif n >= 4:
        return romanMe(n-4, s+'IV')
    elif n >= 1:
        return romanMe(n-1, s+'I')
    return s

with open(sys.argv[1]) as f:
    for line in f:
        n = int(line.strip())
        print romanMe(n)
