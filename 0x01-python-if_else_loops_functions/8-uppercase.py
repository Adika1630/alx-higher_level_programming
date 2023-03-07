#!/usr/bin/python3

def upper(str):
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            x = chr(ord(x)-32)
        print('{}'.format(x), end='')
    print("")
