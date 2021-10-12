#!/usr/bin/python3
"""reads from a file and prints"""



def read_file(filename=""):
    """Reads from filename and prints
    its contents to stdout
    filename is name of the file"""


    with open(filename, encoding="utf-8") as f:
        read_text = f.read()
        print(read_text, end="")
