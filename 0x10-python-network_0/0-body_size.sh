#!/bin/bash
#A bash scrit that takes a URL and displays the size of the body
curl -sI "$1" | grep "Content-Length" | awk '{print $2}'
