#!/usr/bin/python3
"""This is  base module that provides a base for other classes"""


import csv
import json
import os
import turtle


class Base:
    """Creating a base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """defining the attributes of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects