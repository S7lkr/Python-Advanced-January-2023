numbers = tuple(map(float, input().split(" ")))
occurrences = {num: numbers.count(num) for num in numbers}

[print(f"{k} - {v} times") for k, v in occurrences.items()]


# numbers = [float(n) for n in input().split(" ")]
# occurrences = {}
#
# for num in numbers:
#     if num not in occurrences.keys():
#         occurrences[num] = 0
#     occurrences[num] += 1
#
# [print(f"{key} - {value} times") for key, value in occurrences.items()]