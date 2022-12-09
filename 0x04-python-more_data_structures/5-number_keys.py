#!/usr/bin/python3

def number_keys(a_dictionary):
    """returns the number of keys in a dictionary"""
    keys = a_dictionary.keys()
    count = 0
    for a in a_dictionary:
        count += 1
    return count
