#!/usr/bin/python3
"""A Python script that takes 2 arguments in order to solve this challenge."""

import sys
import requests

if __name__ == "__main__":
    url = "https://developer.github.com/v3/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pasis
