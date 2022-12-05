#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Reverses elements in a list"""
    length = 0
    for i in my_list:
        length += 1
    i = 0
    while (i < (length)):
        temp = my_list[i]
        my_list[i] = my_list[length - 1]
        my_list[length - 1] = temp
        i += 1
        length -= 1

    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
