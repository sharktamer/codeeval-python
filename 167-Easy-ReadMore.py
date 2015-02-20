#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if len(line) > 55:
            line = line[:40]
            if ' ' in line:
                line = ' '.join(line[:40].split(' ')[:-1])
            print '{0}... <Read More>'.format(line)
        else:
            print line

