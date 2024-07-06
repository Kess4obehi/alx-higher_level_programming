#!/usr/bin/bash
"""A Python script that takes in a URL, sends a request ad display value"""

import requests
import sys

if __name__ = "__main__":
    url = sys.argv.[1]
    req = requests.get(url)
    print(req.header.get("X-Request-Id")
