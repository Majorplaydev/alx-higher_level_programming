#!/usr/bin/python3

""" A square class based on the last square class"""

class Square:
    """ Initialization of the square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Sets the current size of the square."""
        return self.__size

    @property
    def position(self):
        """Gets the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Gives result on the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character."""
        if self.__size == 0:
            print()
            return

        print("\n" * self.position[1], end="")
        print("\n".join([" " * self.position[0] +
                        "#" * self.size
                         for i in range(self.size)]))
