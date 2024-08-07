#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request ad display value"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
