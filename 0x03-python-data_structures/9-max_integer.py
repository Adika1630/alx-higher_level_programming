#!/usr/bin/python3
def max_integer(my_list=[]):
    y = 0
    if my_list is None:
        return None
    for x in my_list:
        if y == 0 or y < x:
            y = x
    return y
