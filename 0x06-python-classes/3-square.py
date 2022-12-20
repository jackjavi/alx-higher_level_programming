#!/usr/bin/python3
"""Define a square class"""


class Square:
    """
    Initialize the square class.

    Args:
        size: size of suare.
    """
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
