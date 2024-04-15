#!/usr/bin/python3

""" creating a subclass from a parent class called list"""


class MyList(list):
    """ A class that was inherited from List"""
    def print_sorted(self):
        """ A function that prints a sorted list"""
        print(sorted(self))
