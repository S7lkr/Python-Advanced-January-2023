def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))  # 1st priority, 2nd priority
    result = []
    for cheese, amount in sorted_data:
        result.append(cheese)
        result.extend(sorted(amount, key=lambda num: -num))     # equal to "reverse=True"
    return "\n".join(list(map(str, result)))


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)