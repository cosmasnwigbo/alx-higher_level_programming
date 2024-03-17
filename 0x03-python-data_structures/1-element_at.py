#!/usr/bin/python3

# my_list, idx -  function that retrieves an element from a list
# @my_list, idx both are parameter of function


def element_at(my_list, idx):
    if idx < 0:
        return(None)
    elif idx > len(my_list):
        return(None)
    else:
        return(my_list[idx])
