#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b

    except (ZeroDivisionError, FloatingPointError):
        result = None
    finally:
        print("inside result: {}".format(result))
    return (result)
