#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max(a_dictionary.values(), default=None)
        for key, value in a_dictionary.items():
            if value == max:
                return key
    return None
