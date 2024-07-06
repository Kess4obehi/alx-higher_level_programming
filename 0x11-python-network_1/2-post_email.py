#!/usr/bin/python3
"""A Python script that takes in a URL and an email, sends a POST request"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    #define the value to be posted
    value = {"email": sys.argv[2]}
    #encode the value
    data = urllib.parse.urlencode(value).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
