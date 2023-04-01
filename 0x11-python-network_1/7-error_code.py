#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./7-error_code.py <URL>
    - Handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
