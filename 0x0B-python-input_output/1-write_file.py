#!/usr/bin/python3
"""creating a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Write a string to a UTF"""

    with open(filename, "w", encoding="utf-8") as f:
    return f.write(text)
