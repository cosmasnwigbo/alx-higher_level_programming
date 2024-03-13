#!/usr/bin/python3

# def islower(c) - a function that checks for lowercase character
# @c: parameter of function c
# Return: True otherwise False


def islower(c):
    if (type(c) is int):
        return (False)
    elif(ord('a') <= ord(c) <= ord('z')):
        return(True)
    return(False)
