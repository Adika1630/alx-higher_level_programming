#!/usr/bin/python3

for x in range(122, 96, -1):
    if x % 2 != 0:
        print("{}".format(chr(x - 32)), end="")
    else:
        print("{}".format(chr(x)), end="")
