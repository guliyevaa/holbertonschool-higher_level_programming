#!/usr/bin/env bash
from urllib import request

response = request.urlopen("https://intranet.hbtn.io/status")
html = response.read()
print(html)
