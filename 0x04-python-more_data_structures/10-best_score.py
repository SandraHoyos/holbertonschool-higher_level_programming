#!/usr/bin/python
def best_score(a_dictionary):
    if a_dictionary:
        maxi = max(a_dictionary.values(), default= None)
        for key, value in a_dictionary.items():
            if value == maxi:
                return key
    return None
