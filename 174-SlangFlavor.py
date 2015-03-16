#!/bin/env python

import sys
from itertools import cycle

phrases = [
    ', yeah!',
    ', this is crazy, I tell ya.',
    ', can U believe this?',
    ', eh?',
    ', aw yea.',
    ', yo.',
    '? No way!',
    '. Awesome!'
]
phrase_cycle = cycle(phrases)

with open(sys.argv[1]) as f:
    text = f.read().strip()


