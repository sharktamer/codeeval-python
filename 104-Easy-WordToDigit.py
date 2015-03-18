#!/bin/env python

import sys

numbers = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    out = ''.join(numbers[i] for i in line.split(';'))
    print(out)
