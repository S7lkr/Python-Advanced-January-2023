def grocery_store(**kwargs):
    result = []
    for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        result.append([k, v])
    return "\n".join([": ".join(list(map(str, lst))) for lst in result])


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))