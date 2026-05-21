#!/usr/bin/env python3


import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    while len(s) < 8:
        s += "Z"
    print(s)

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)