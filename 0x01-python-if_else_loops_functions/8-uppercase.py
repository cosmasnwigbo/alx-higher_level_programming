#!/usr/bin/python3
# uppercase(str) - function that prints a string in uppercase
# @str: parameter of function 
# Return: str


def uppercase(str):
    for x in (str):
        if ord('a') <= ord(x) <= ord('z'):
            x = ord(x) - 32
            print(chr(x), end="")
        else:
            print(x, end="")
    print()

