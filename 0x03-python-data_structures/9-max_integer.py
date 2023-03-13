#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    m = my_list[0]
    for x in my_list:
        if x > m:
            m = x
    return (m)
