#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"  # noqa: E501
str = str.split("object-")[1].split(" language")[0]
print("object-" + str + " with Python")
