#!/bin/bash
# cURL body size

$ curl -Is "$1" | grep -i Content-Length | awk '{print $2}'
