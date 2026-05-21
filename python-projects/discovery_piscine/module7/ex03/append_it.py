#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for arg in args:
        if arg.find("ism", len(arg) - 3) == -1:
            print(arg + "ism")