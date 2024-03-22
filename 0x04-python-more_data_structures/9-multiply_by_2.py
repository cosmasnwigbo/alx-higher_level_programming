#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dic = {}
    value = a_dictionary.values()
    for key in a_dictionary:
        a_dictionary[key] *= 2
    new_dic = a_dictionary[key]

    return (a_dictionary)
