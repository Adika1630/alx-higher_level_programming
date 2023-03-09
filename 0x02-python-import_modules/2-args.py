#!/usr/bin/python3
import sys


def main(*argv):
    i = 0
    n = len(sys.argv) - 1
    if n == 1:
        print("{:d} argument:".format(n))
    elif n == 0:
        print("{:d} arguments.".format(n))
    else:
        print("{:d} arguments:".format(n))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1


if __name__ == "__main__":
    main()
