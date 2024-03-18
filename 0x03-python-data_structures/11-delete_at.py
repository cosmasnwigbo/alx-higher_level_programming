#!/usr/bin/python3
# delete_at - a function that deletes the item at a specific position in a list
# @my_list, idx: parameter of function delete_at
# Return: my_list


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return (my_list)
    elif idx == len(my_list):
        idx = (len(my_list) - 1)
        del my_list[idx]
    else:
        del my_list[idx]
    return (my_list)
