#!/usr/bin/python3

def uppercase(str):
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            x = chr(ord(x)-32)
        print('{}'.format(x), end='')
    print("")
