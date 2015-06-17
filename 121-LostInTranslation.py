#!/usr/bin/env python

import sys

map_dict = {'a': 'y',
            'b': 'h',
            'c': 'e',
            'd': 's',
            'e': 'o',
            'f': 'c',
            'g': 'v',
            'h': 'x',
            'i': 'd',
            'j': 'u',
            'k': 'i',
            'l': 'g',
            'm': 'l',
            'n': 'b',
            'o': 'k',
            'p': 'r',
            'q': 'z',
            'r': 't',
            's': 'n',
            't': 'w',
            'u': 'j',
            'v': 'p',
            'w': 'f',
            'x': 'm',
            'y': 'a',
            'z': 'q',
            ' ': ' '}

with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    out = ''.join(map_dict[i] for i in line)
    print(out)
