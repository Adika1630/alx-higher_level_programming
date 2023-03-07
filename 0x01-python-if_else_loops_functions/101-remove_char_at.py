#!/usr/bin/python3

def remove_char_at(str, n):
    str2 = ''
    if n > len(str) or n < 0:
        return str
    for x in str:
        if x != str[n]:
            str2 += x
    return str2
