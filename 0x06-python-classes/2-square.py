#!/usr/bin/python3

"""Write a class Square that defines a square by:(based on 1-square.py)"""


class Square:
    """A Square class representation"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
