def items_finder():
    cks, decs, gfts = 0, 0, 0
    santa_pos = 0, 0
    for row in range(rows):
        for col in range(cols):
            cell = north_pole[row][col]
            if cell == "Y":
                santa_pos = row, col
            elif cell == "C":
                cks += 1
            elif cell == "D":
                decs += 1
            elif cell == "G":
                gfts += 1
    return santa_pos, cks, decs, gfts


def index_check(a, b):
    if a < 0:
        a = rows - 1
    elif a >= rows:
        a = 0
    if b < 0:
        b = cols - 1
    elif b >= cols:
        b = 0
    return a, b


rows, cols = list(map(int, input().split(", ")))
north_pole = [input().split(" ") for _ in range(rows)]

cookies_collected = 0
decorations_collected = 0
gifts_collected = 0
field_empty = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
santa_start, cookies, decorations, gifts = items_finder()
r, c = santa_start
command = input()

while command != "End":
    way, steps = command.split("-")
    for _ in range(int(steps)):              # ["left", "3"]
        x, y = directions[way]
        north_pole[r][c] = "x"
        r, c = r+x, c+y
        r, c = index_check(r, c)
        if north_pole[r][c] == "C":
            cookies -= 1
            cookies_collected += 1
        elif north_pole[r][c] == "D":
            decorations -= 1
            decorations_collected += 1
        elif north_pole[r][c] == "G":
            gifts -= 1
            gifts_collected += 1
        north_pole[r][c] = "Y"
        if not cookies and not decorations and not gifts:
            field_empty = True
            break
    if field_empty:
        break
    command = input()

if field_empty:
    print("Merry Christmas!")

print(f"You've collected:\n- {decorations_collected} Christmas decorations\n- {gifts_collected} Gifts\n"
      f"- {cookies_collected} Cookies")

[print(' '.join(row)) for row in north_pole]