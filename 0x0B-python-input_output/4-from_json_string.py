#!/usr/bin/python3
""" defines a json object"""


def from_json_string(my_str):
    """load to json from str
    Args
       my_str
    """
    import json
    return(json.loads(my_str))
