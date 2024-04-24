number_of_digits = list(map(int, input().split(" ")))

set_1 = {input() for _ in range(number_of_digits[0])}
set_2 = {input() for _ in range(number_of_digits[1])}

result = set_1.intersection(set_2)
print("\n".join(result))