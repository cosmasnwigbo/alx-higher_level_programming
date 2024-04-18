#!/usr/bin/python3

"""
A module documentaion for python class
"""


class Square:
    """
    A class square definition that takes a private attribute named size
    """

    def __init__(self, size=0):
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
