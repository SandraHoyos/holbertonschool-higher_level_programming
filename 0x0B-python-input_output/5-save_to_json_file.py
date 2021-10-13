#!/usr/bin/python3
import json
"""
This file contains a function that
writes an obj to a text file using
JSON rep
"""


def save_to_json_file(my_obj, filename):
    """save to json file
    Args
       my_obj
       filename
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, myFile)
