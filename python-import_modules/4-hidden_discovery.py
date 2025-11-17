#!/usr/bin/python3
import dis
import marshal
import types

if __name__ == "__main__":
    filename = "/tmp/hidden_4.pyc"

    with open(filename, "rb") as f:
        f.read(16)  # skip the header of the .pyc file
        code = marshal.load(f)

    names = set()

    def walk_code(c):
        if isinstance(c, types.CodeType):
            for name in c.co_names:
                if not name.startswith("__"):
                    names.add(name)
            for const in c.co_consts:
                walk_code(const)

    walk_code(code)

    for name in sorted(names):
        print(name)
