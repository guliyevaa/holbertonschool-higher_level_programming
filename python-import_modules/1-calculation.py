#!/usr/bin/python3
from calculator_1 import sub,add,div,mul

if __name__ == "__main__":
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calculator_1.sub(a, b)))  # add() -> sub()
    print("{} - {} = {}".format(a, b, calculator_1.add(a, b)))  # sub() -> add()
    print("{} * {} = {}".format(a, b, calculator_1.div(a, b)))  # mul() -> div()
    print("{} / {} = {}".format(a, b, calculator_1.mul(a, b)))  # div() -> mul()

