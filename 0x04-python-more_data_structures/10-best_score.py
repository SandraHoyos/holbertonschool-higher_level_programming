#!/usr/bin/python
def best_score(a_dictionary):
    if a_dictionary:
        return max(a_dictionary.values(), default=None)
    return None
