#!/bin/env python

import sys
#!/bin/env python

import sys
from itertools import groupby

with open(sys.argv[1]) as f:
    for line in f:
        nums = ''.join(sorted(line.split()))
        grouped = [list(g) for v, g in groupby(nums)]
        unique = [i for i in grouped if len(i) == 1]
        if unique:
            print(line.find(unique[0][0]) // 2 + 1)
        else:
            print(0)

