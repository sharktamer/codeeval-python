#!/bin/env python

for i in xrange(1, 13):
    for j in xrange(1, 13):
        print(str(i * j).rjust(4)),
    print
