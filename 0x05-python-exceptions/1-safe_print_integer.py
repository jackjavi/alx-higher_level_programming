#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer with "{:d}".format().

    Args:
        value: value of any type

    Returns:
        Returns True if value has been correctly printed
        Otherwise, returns False
    """
    try:
        print("{:d}".format(int(value)))
	return (True)
    except (ValueError, TypeError):
        return (False)
