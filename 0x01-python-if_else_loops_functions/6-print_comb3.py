#!/usr/bin/python3

i = 1
for x in range(9):
    for y in range(i, 10):
        if i != 9:
            print('{:d}{:d}, '.format(x, y), end="")
        else:
            print('{:d}{:d}'.format(x, y))

    i += 1
