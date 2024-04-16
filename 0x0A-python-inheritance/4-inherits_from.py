#!/usr/bin/python3
""" Return Only sub class of a class """


def inherits_from(obj, a_class):
    """
    Return true if the object is an instance of a class
    """
    if type(obj) is a_class:
        return false
    else:
        return isinstance(obj, a_class)
