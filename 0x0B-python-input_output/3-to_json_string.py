#!/usr/bin/python3
""" return the JSON representation of an object"""


import json


def to_json_string(my_obj):
    """a JSON to string functio
    arg:
    my_obj string to represent
    return: the Json representation
    of an on¡bject"""

    return json.dumps(my_obj)
