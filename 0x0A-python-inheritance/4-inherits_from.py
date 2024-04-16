#!/usr/bin/python3
"""Return only subclass of a classs"""


def inherits_from(obj, a_class):
    """a function that determines if an object
    is an instance of a class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
