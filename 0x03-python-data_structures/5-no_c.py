#!/usr/bin/python3
def no_c(my_string):
    trans_dic = {ord('c'): None, ord('C'): None}
    new_string = my_string.translate(trans_dic)
    return new_string
