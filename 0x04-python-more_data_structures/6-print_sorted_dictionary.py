#!/usr/bin/python3



def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary.keys())
    for keys in sorted_key:
        value = a_dictionary[keys]
        print(f"{keys}: {value}")


