from collections import deque

materials = list(map(int, input().split(" ")))
magic_levels = deque(list(map(int, input().split(" "))))

crafted = []

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[0] else 0
    magic = magic_levels.popleft() if material or not magic_levels[0] else 0
    if not magic:
        continue
    product = material * magic
    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic)
    else:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

[print(f"{present}: {crafted.count(present)}") for present in sorted(set(crafted))]


# from collections import deque
#
#
# def present_validator(res):
#     if res == 150 or res == 250 or res == 300 or res == 400:
#         return present_maker(res)
#     materials.append(material + 15)
#
#
# def present_maker(res):
#     if res == 150:
#         presents["Doll"] += 1
#     elif res == 250:
#         presents["Wooden train"] += 1
#     elif res == 300:
#         presents["Teddy bear"] += 1
#     elif res == 400:
#         presents["Bicycle"] += 1
#
#
# materials = list(map(int, input().split(" ")))
# magic_levels = deque(list(map(int, input().split(" "))))
#
# presents = {
#     "Doll": 0,
#     "Wooden train": 0,
#     "Teddy bear": 0,
#     "Bicycle": 0
# }
#
# while materials and magic_levels:
#     material = materials.pop()
#     magic = magic_levels.popleft()
#     if material == 0 and magic == 0:
#         continue
#     elif material == 0:
#         magic_levels.appendleft(magic)
#         continue
#     elif magic == 0:
#         materials.append(material)
#         continue
#     result = material * magic
#     if result > 0:
#         present_validator(result)
#     else:
#         materials.append(material + magic)
#
# presents = {k: v for k, v in presents.items() if v != 0}
#
# if "Doll" in presents.keys() and "Wooden train" in presents.keys() or \
#         "Teddy bear" in presents.keys() and "Bicycle" in presents.keys():
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
#
# if materials:
#     print(f"Materials left: {', '.join(map(str, materials[::-1]))}")
# if magic_levels:
#     print(f"Magic left: {', '.join(map(str, magic_levels))}")
#
# [print(f"{k}: {v}") for k, v in sorted(presents.items())]