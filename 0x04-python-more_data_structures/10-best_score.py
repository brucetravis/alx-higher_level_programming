def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    max_score = max(a_dictionary.values())
    best_key = [key for key, value in a_dictionary.items()
                if value == max_score][0]
    return best_key
