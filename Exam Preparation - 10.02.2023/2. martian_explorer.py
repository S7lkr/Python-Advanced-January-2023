def border_check(row, col):
    if row < 0:
        row = 5
    elif 6 == row:
        row = 0
    if col < 0:
        col = 5
    elif 6 == col:
        col = 0
    return row, col


mars = [input().split(" ") for _ in range(6)]
r, c = 0, 0

water = 0
metal = 0
concrete = 0

located = False
for a in range(6):
    if located:
        break
    for b in range(6):
        if mars[a][b] == "E":
            r, c = a, b
            located = True
            break

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
commands = input().split(", ")

for way in commands:
    x, y = directions[way]
    r, c = r + x, c + y
    r, c = border_check(r, c)
    if mars[r][c] == "W":
        print(f"Water deposit found at ({r}, {c})")
        water += 1
    elif mars[r][c] == "M":
        print(f"Metal deposit found at ({r}, {c})")
        metal += 1
    elif mars[r][c] == "C":
        print(f"Concrete deposit found at ({r}, {c})")
        concrete += 1
    elif mars[r][c] == "R":
        print(f"Rover got broken at ({r}, {c})")
        break

if water + metal + concrete >= 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")