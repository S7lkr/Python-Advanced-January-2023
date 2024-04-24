def even_odd_filter(**numbers):
    for num_type in numbers.keys():
        if num_type == "even":
            numbers["even"] = list(filter(lambda x: x % 2 == 0, numbers["even"]))
        elif num_type == "odd":
            numbers["odd"] = list(filter(lambda x: x % 2 == 1, numbers["odd"]))
        continue
    return dict(numbers)


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))