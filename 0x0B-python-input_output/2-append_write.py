#!/usr/bin/python3
"""appends a string at the end of
a text file"""


def append_write(filename="", text=""):
    """append a stringe to the end of a UTF8 text file
    arg:
    filename: name of the file
    text: text to append
    return: the number of characters added"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
