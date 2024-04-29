def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_kids, naughty_kids = [], []
    result = []

    def place_kid():
        if len(kids) == 1:
            nice_kids.extend(kids) if type_kid == "Nice" else naughty_kids.extend(kids)
            santa_list.remove(*kids)

    for data in args:
        num, type_kid = data.split("-")         # ["3", "Nice"]
        kids = [(n, kid_name) for n, kid_name in santa_list if n == int(num)]
        place_kid()
    for kid_kw, type_kid in kwargs.items():
        kids = [(num, kid_name) for num, kid_name in santa_list if kid_kw == kid_name]
        place_kid()

    if nice_kids:
        result.append(f"Nice: {', '.join(k[1] for k in nice_kids)}")
    if naughty_kids:
        result.append(f"Naughty: {', '.join(k[1] for k in naughty_kids)}")
    if santa_list:
        result.append(f"Not found: {', '.join(k[1] for k in santa_list)}")

    return "\n".join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

