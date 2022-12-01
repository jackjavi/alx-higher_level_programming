#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic operations"""
    import sys
    from calculator_1 import add, sub, mul, div

    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if (len(sys.argv)) < 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    if operator != ('+' or '-' or '/' or '*'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
