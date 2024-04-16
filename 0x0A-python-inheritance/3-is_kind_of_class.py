#!/usr/bin/python3
"""Checks if object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instnce of a class
    or a class that the class is inhrited from
    """
    return (isinstance(obj, a_class))
