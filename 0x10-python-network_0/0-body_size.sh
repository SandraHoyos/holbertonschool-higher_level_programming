#!/bin/bashh~
# cURL body size

$ curl -sI $URL | grep -i Content-Length | awk '{print $2}'
