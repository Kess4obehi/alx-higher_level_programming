#!/usr/bin/python3
"""A function that adds two integer or floats"""


def add_integer(a, b=98):
    """A function that returns the addition of two integers"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("a must be an integer")
    return (int(a) + int(b))
