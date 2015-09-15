#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    length = int(line)
    # r = [str(i) for i in range(int('1'+'0'*(length-1)), int('1'+'0'*length))]
    r = ('{n:0{l}d}'.format(n=i, l=length)
         for i in range(0, int('1'+'0'*length)))
    lucky = [i for i in r
             if len({sum(int(j) for j in k)
                     for k in (i[:len(i)//2], i[len(i)//2:])}) == 1]
    print(len(lucky))
