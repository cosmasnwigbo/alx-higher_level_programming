#!/usr/bin/python3

"""
A module documentation

"""


class Square:

    """
    a class named square defined here

    """

    def __init__(self, size=0):
        self.__size = size

        @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            print("size  must be  an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= o", end="")
            raise ValueError
        else:
            self.__size = value

    def area(self):
        return (self.__size ** 2)
