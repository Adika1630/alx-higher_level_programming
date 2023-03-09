#!/usr/bin/python3
import sys


def main(*argv):
    i = 0
    l = len(sys.argv) - 1
    if l == 1:
        print("{:d} argument:".format(l))
    elif l == 0:
        print("{:d} arguments.".format(l))
    else:
        print("{:d} arguments:".format(l))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1


if __name__ == "__main__":
    main()
