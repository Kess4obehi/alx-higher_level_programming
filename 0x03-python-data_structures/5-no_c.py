#!/usr/bin/python3
def no_c(my_string):
    chars_to_remove = "cC"
    modified_string = ""
    for char in my_string:
        if char not in chars_to_remove:
            modified_string += char

    return (modified_string)
