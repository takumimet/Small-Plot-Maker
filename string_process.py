""" This script contains functions to process the string entries
    in home_gui.py """

# Raised when parameters are not numerical
class NotANumber(ValueError):
    pass

def string_to_int(phrase: str) -> list:
    """ Creates a list of numericals
        from a string phrase.         """
    try:
        # Create a list of items in phrase
        phrase_list = phrase.split(", ")
        # Convert to numericals


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
    pass

def only_letters(names: str) -> bool:
    pass