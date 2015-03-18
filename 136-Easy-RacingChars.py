#!/bin/env python

import sys

last_gate = None
with open(sys.argv[1]) as f:
    for line in f:
        match_char = ('_', 'C')['C' in line]
        curr_pos = line.find(match_char)
        if last_gate is None or curr_pos == last_gate:
            direction = '|'
        elif curr_pos < last_gate:
            direction = '/'
        else:
            direction = '\\'
        out = line.replace(match_char, direction).strip()
        print(out)
        last_gate = curr_pos

