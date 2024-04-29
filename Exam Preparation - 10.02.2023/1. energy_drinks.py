from collections import deque

caffeine_mg = input().split(", ")
energy_drinks = deque(input().split(", "))
total_caffeine = 0

while energy_drinks and caffeine_mg:
    caff = caffeine_mg.pop()
    drink = energy_drinks.popleft()
    if total_caffeine + (int(caff) * int(drink)) >= 300:
        energy_drinks.append(drink)
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0
    else:
        total_caffeine += int(caff) * int(drink)
else:
    if energy_drinks:
        print(f"Drinks left: {', '.join(energy_drinks)}")
    else:
        print("At least Stamat wasn't exceeding the maximum caffeine.")


print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")