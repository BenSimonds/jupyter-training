"""Some excellent functions that I wrote myself."""


def backwards(string):
    """reverses a string"""
    
    # Python lists have a handy reverse() method, but strings dont.
    # Lets convert our string to a list and then reverse it.
    string_as_list = list(string)

    # Reverse it.
    string_as_list.reverse()
    
    # return it converted back to a list by joining the letters together with an empty string.
    return ''.join(string_as_list)

