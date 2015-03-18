#!/bin/env python

import sys

with open(sys.argv[1]) as f:
    for line in f:
        # Split the line on semicolon, then each split by word
        words, num_strings = [i.split() for i in line.split(';')]
        # Convert the number strings into ints
        nums = [int(i) for i in num_strings]
        nums += [i for i in range(1, len(nums) + 2) if i not in nums]
        out = ' '.join(i[1] for i in sorted(zip(nums, words)))
        print(out)
