from collections import deque

cups_capacity = deque([int(i) for i in input().split(" ")])
bottles = [int(j) for j in input().split(" ")]
wasted_water = 0
failed = False

while cups_capacity:
    last_bottle = bottles.pop()
    if last_bottle >= cups_capacity[0]:
        wasted_water += last_bottle - cups_capacity.popleft()
    else:
        cups_capacity[0] -= last_bottle
    if not bottles:
        failed = True
        break
else:
    print("Bottles:", *bottles, sep=' ')

if failed:
    print("Cups:", *cups_capacity, sep=" ")
print(f"Wasted litters of water: {wasted_water}")