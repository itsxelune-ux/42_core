#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    # upper_args = [args.upper() for args in sys.argv]
    # print(upper_args)
    for arg in sys.argv[1:]:
        print(arg.lower())