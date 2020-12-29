""" This script contains functions to process the string entries
    in home_gui.py """

import random

# Raised when parameters are not numerical
class NotANumber(ValueError):
    pass

def string_to_int(phrase: str) -> list:
    """ Creates a list of numericals
        from a string phrase.         """
    try:
        output = []
        # Create a list of items in phrase
        for item in phrase.split(", "):
            if has_decimals(item):
                output.append(float(item))
            else:
                output.append(int(item))
        
        return output

    except ValueError:
        raise NotANumber("Entry can only contain numericals")    

def string_to_list(phrase: str) -> list:
    """ Creates a list of strings
        from a string phrase.      """    
        # Create a list of items in phrase
    return phrase.split(", ")

def has_decimals(number: str) -> bool:
    """ Checks if a string numerical
        is a decimal number           """
    # TODO It might work better with regex
    if '.' in number:
        return True
    return False

def only_letters(names: str) -> bool:
    pass


if __name__ == '__main__':
    assert string_to_int("1, 2, 3, 4, 5, 6, 7, 8, 9") == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert string_to_int("1, 4, 9, 16, 25, 36, 49, 64, 81") == [1, 4, 9, 16, 25, 36, 49, 64, 81]
    assert string_to_int("1, 2, 3, 4.5, 5, 6, 7, 8, 9.3") == [1, 2, 3, 4.5, 5, 6, 7, 8, 9.3]
    assert string_to_list("1, 2, 3, 4, 5, 6, 7, 8, 9") == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]