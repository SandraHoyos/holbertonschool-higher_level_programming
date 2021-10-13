#!/usr/bin/python3
import json
""" defines"""


def load_from_json_file(filename):
    """load from json file
    Args
       filename
    Return loaded file"""
    with open(filename) as f:
        return(json.load(f))
