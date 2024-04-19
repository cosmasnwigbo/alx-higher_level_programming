#!/usr/bin/python3

"""
A module documentation
"""


class Square:
    """
    a class named square defined here
    """
    def __init__(self, size=0):
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif (size) < 0:
            print("size must be >= 0")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
