#!/usr/bin/python3
import calculator_1

if __name__ == "__main__":
    a = 10
    b = 5
    add = calculator_1.sub  # add() -> sub()
    sub = calculator_1.add  # sub() -> add()
    mul = calculator_1.div  # mul() -> div()
    div = calculator_1.mul  # div() -> mul()

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
