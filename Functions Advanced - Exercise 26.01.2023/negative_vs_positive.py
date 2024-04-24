numbers = list(map(int, input().split(" ")))

positive_numbers = sum([n for n in numbers if n > 0])
negative_numbers = sum([m for m in numbers if m < 0])

print(negative_numbers)
print(positive_numbers)

if positive_numbers > abs(negative_numbers):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")