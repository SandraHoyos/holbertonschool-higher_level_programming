#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        maxi = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == maxi:
                return key
    return None
