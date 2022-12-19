#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer with "{:d}".format().

    Args:
        value: The integer to print

    Returns:
        Returns True if value has been correctly printed
        Otherwise, returns False if TypeError or ValueError occurs
    """
    try:
        print("{:d}".format(int(value)))
    except (ValueError, TypeError):
        return (False)
    return (True)
