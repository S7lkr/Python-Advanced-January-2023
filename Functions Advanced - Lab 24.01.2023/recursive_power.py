def recursive_power(n, power):
    if power == 0:
        return 1
    elif power == 1:
        return n
    return n * recursive_power(n, power - 1)


# def recursive_power(num, power):
#     result = num ** 2
#
#     recursive_power(num, power)
#
#
print(recursive_power(2, 10))