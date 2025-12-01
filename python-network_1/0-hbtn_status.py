#!/usr/bin/python3
from urllib import request

response = request.urlopen("https://intranet.hbtn.io/status")
html = response.read()
print(html)
