from collections import deque

chocolates = list(map(int, input().split(", ")))
cups_of_milk = deque(list(map(int, input().split(", "))))
milkshakes = 0

# UNTIL: milkshakes LESS than 5, enough chocolate and enough milk, keep mixing.
# if we have 5 milkshakes OR any of the ingredients is depleted, STOP.
while milkshakes < 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    milk_cup = cups_of_milk.popleft()
    if chocolate <= 0 and milk_cup <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(milk_cup)
        continue
    elif milk_cup <= 0:
        chocolates.append(chocolate)
        continue
    if chocolate == milk_cup:
        milkshakes += 1
    else:
        chocolates.append(chocolate - 5)
        cups_of_milk.append(milk_cup)

# Finally, we will make 3 INDIVIDUAL CHECKS:
# are there 5 milkshakes??
if milkshakes == 5:     # YES
    print("Great! You made all the chocolate milkshakes needed!")
else:   # or NO
    print("Not enough milkshakes.")

# is any chocolates left??      YES                      NO
print(f"Chocolate: {', '.join(map(str, chocolates)) or 'empty'}")

# is there any milk??       YES                       NO
print(f"Milk: {', '.join(map(str, cups_of_milk)) or 'empty'}")