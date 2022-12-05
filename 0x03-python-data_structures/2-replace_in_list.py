#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position"""
    if (idx < 0) or (((len(my_list)) - 1) > idx):
        return (my_list)
    else:
        my_list[idx] = new_element
        return (my_list)
