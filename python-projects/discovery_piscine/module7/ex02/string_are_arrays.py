#!/usr/bin/env python3

#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    result = ""

    for char in string:
        if char == "z":
            result += "z"

    if result == "":
        print("none")
    else:
        print(result)