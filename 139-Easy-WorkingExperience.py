#!/bin/env python

import sys
from datetime import datetime
from calendar import monthrange

# Read all lines from file supplied as first argument
with open(sys.argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    # Create a list of date object pairs for each date range in the line
    date_periods = [
        [datetime.strptime(d, '%b %Y') for d in i.split('-')]
        for i in line.split('; ')
    ]
    # Sort the date ranges by begin date
    date_periods.sort(key=lambda x: x[0])
    # Create an output list and store the first date range in it for comparison
    out = [date_periods.pop(0)]
    for d in date_periods:
        d1, d2 = out[-1], d
        # If the end of the last date is after the start of the next date...
        if d1[-1] >= d2[0]:
            # Set the end of the last date to whichever date has the later end
            out[-1] = [d1[0], max(d1[-1], d2[-1])]
        else:
            # if not, add the current date range to the out list
            out += [d2]
    # Sum the size of each range, taking the last day of the month for each end
    result = sum(((d2 - d1).days + monthrange(d2.year, d2.month)[1]) / 365
                 for d1, d2 in out)
    # Print the result :D
    print(int(result))
