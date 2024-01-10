#!/usr/bin/python3

"""A class Square that defines a square by the last square file:(based on 3-square.py)"""


class Square:
    """Square class initialization"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Sets current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Get the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Gives result of the current square area"""
        return (self.__size * self.__size)
