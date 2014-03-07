#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
    for line in f:
        numbers = [int(i) for i in line.split(',')]
        counts = {i: len([j for j in numbers if j == i]) for i in numbers}
        output = [i for i in counts if counts[i] > len(numbers) / 2]
        if len(output) == 0:
            print None
        else:
            print output[0]
