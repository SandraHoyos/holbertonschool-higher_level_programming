#!/bin/bash
# cURL body size
curl -Is "$1" | grep "Content-Length" | cut -d' ' -f 2
