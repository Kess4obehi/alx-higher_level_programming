#!/usr/bin/python

def safe_print_division(a, b):
    try:
        div = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {:d}".format(div))
        return div
