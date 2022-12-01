#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    if (len(sys.argv)) < 2:
        print("0 arguments.")
    elif (len(sys.argv) == 2):
        print("1 argument.")
    else:
        print("{} arguments: ".format(len(sys.argv)))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
