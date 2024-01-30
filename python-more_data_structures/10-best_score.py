#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score = max(a_dictionary.values())
    bst_st = [key for key, value in a_dictionary.items() if value == max_score]
    return bst_st[0] if bst_st else None
