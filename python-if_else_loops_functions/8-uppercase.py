#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)  # kiçik hərfi böyük hərfə çevir
        else:
            result += c  # digər simvollar olduğu kimi qalır
    print(result)
