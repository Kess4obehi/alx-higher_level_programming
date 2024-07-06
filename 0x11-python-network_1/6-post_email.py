#!/usr/bin/python3
"""A Python script that takes in a URL and an email addressand send post request"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url, ({"email": email}))
    print("req.text")
