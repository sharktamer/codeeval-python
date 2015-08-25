#!/usr/bin/env python

import sys

out = ('BigEndian', 'LittleEndian')[sys.byteorder == 'little']
print(out)
