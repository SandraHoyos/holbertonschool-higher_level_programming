#!/bin/bash
# cURL body size

curl -Is "$1" | grep "Content-Length" | awk '{print $2}'
