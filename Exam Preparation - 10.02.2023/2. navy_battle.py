def cruiser_hit(ships):
    return ships - 1


def mine_hit(hull):
    return hull - 1


size = int(input())
battlefield = [list(input()) for _ in range(size)]
row, col = 0, 0
sub_hp = 3
cruisers = 3

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for a in range(size):
    for b in range(size):
        if battlefield[a][b] == "S":
            row, col = a, b

command = input()
while cruisers:
    x, y = directions[command]
    battlefield[row][col] = "-"
    row, col = row + int(x), col + int(y)
    if battlefield[row][col] == "*":
        sub_hp = mine_hit(sub_hp)
    elif battlefield[row][col] == "C":
        cruisers = cruiser_hit(cruisers)
    battlefield[row][col] = "S"

    if sub_hp < 1:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
        break
    command = input()
else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

[print("".join(row)) for row in battlefield]
