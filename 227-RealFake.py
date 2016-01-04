#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    nums = line.replace(' ', '')
    card_sum = sum(int(i) if n % 2 else int(i) * 2 for n, i in enumerate(nums))
    if card_sum % 10:
        print('Fake')
    else:
        print('Real')
