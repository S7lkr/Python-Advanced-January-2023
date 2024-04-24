from functools import reduce


def operate(sign, *args):
    operations = {
        "+": lambda x: sum(x),
        "-": lambda x: reduce(lambda a, b: a - b, x),
        "*": lambda x: reduce(lambda a, b: a * b, x),
        "/": lambda x: reduce(lambda a, b: a / b, x),
    }
    return operations[sign](args)


print(operate("*", 3, 4))