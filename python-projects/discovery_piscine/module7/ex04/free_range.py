#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])

        if start >= end:
            print("none")
        else:
            numbers = list(range(start, end + 1))
            print(numbers)
    except ValueError:
        # In case parameters are not numbers
        print("none")