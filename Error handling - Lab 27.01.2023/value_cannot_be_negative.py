class ValueCannotBeNegative(Exception):     # always define our "custom exception" as a class
    pass    # no init func!


numbers = [int(input()) for _ in range(5)]

for num in numbers:
    if num < 0:     # if some any number is negative, raise the exception (class)
        raise ValueCannotBeNegative(f"Value cannot be negative number! Convert {num} to {abs(num)}")