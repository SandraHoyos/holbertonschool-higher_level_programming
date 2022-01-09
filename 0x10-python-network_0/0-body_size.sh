#!/bin/bash
# takes in an URL, sends a request to that URL, and displays the size of the body of response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
