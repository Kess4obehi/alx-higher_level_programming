#!/usr/bin/python3
"""creating a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    The created function that returns the number of characters written
    """

    with open(filename, "w", encoding="utf-8") as f:
    return f.write(text)
