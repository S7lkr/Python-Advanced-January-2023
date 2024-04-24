from functools import reduce


def multiply(*args):
    return reduce(lambda x, y: x * y, args)

# def multiply(*args):
#     number = 1
#     for num in args:
#         number *= num
#     return number


print(multiply(1, 4, 5))