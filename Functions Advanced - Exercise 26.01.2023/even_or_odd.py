def even_odd(*args):    # REMEMBER: args (without '*' in front) is a TUPLE
    act = args[-1]
    result = []
    if act == "even":
        [result.append(n) for n in args[:-1] if int(n) % 2 == 0]
    elif act == "odd":
        [result.append(n) for n in args[:-1] if int(n) % 2 == 1]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))