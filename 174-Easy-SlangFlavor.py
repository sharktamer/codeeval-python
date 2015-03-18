#!/usr/bin/env python

import sys
from itertools import cycle, zip_longest
import re

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

sentences = re.findall(r'.*?[\.!?]\n?', text)
out = ''.join(
    i + re.sub(r'[\.!?]', next(phrase_cycle), j)
    for i, j
    in zip_longest(sentences[::2], sentences[1::2], fillvalue='')
)
print(out)
