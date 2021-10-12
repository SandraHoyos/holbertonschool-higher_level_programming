#!/usr/bin/python3

"""write file"""


def write_file(filename="", text=""):
    """writes text in flinename
    arg:
    * filename: name of the file
    * text: string to write in the file
    returns: number of characters written"""


    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
    
