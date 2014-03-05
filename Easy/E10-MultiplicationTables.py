#!/bin/env python

mtable = []
for i in range(1, 13):
    print str(i).rjust(2) + " ".join([str(e*i).rjust(4) for e in range(2, 13)])
