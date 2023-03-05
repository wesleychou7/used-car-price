# my utilities

def remove_nonnumeric(string):
    """
    Removes all non-numeric characters from a given string.

    Args:
        string (str): A string containing both numeric and non-numeric 
        characters.

    Returns:
        str: A new string containing only the numeric characters from the 
        original string.
    """
    return ''.join(c for c in string if c.isnumeric())