from collections import deque

materials = list(map(int, input().split(" ")))
magic_levels = deque(list(map(int, input().split(" "))))

# Gifts:
gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond_jewellery = 0

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    a_sum = material + magic
    if a_sum < 100:
        if a_sum % 2 == 0:
            a_sum = (material * 2) + (magic * 3)
        else:
            a_sum *= 2
    elif a_sum >= 500:
        a_sum /= 2
    if a_sum < 100 or 499 < a_sum:
        continue
    if 100 <= a_sum <= 199:
        gemstone += 1
    elif 200 <= a_sum <= 299:
        porcelain_sculpture += 1
    elif 300 <= a_sum <= 399:
        gold += 1
    elif 400 <= a_sum <= 499:
        diamond_jewellery += 1

if (gemstone and porcelain_sculpture) or (gold and diamond_jewellery):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(list(map(str, materials)))}")
if magic_levels:
    print(f"Magic left: {', '.join(list(map(str, magic_levels)))}")

if diamond_jewellery:
    print(f"Diamond Jewellery: {diamond_jewellery}")
if gemstone:
    print(f"Gemstone: {gemstone}")
if gold:
    print(f"Gold: {gold}")
if porcelain_sculpture:
    print(f"Porcelain Sculpture: {porcelain_sculpture}")