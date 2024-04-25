presents = int(input())
hood_size = int(input())

hood = [input().split(" ") for _ in range(hood_size)]
r, c = 0, 0  # santa's curr pos
nice_kids = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for a in range(hood_size):
    for b in range(hood_size):
        if hood[a][b] == "S":
            r, c = a, b
        elif hood[a][b] == "V":
            nice_kids += 1

nice_kids_left = nice_kids

way = input()
while way != "Christmas morning":
    x, y = directions[way]      # x, y will take that key's value -> (n1, n2)
    if 0 <= r + x < hood_size and 0 <= c + y < hood_size:
        r, c = r + x, c + y
        if hood[r][c] == "V":
            presents -= 1
            nice_kids_left -= 1
        elif hood[r][c] == "C":
            for x, y in directions.values():
                if hood[r + x][c + y] == "V":
                    nice_kids_left -= 1
                    presents -= 1
                elif hood[r + x][c + y] == "X":
                    presents -= 1
                hood[r + x][c + y] = "-"
        hood[r][c] = "S"
        hood[r - x][c - y] = "-"
        if not nice_kids_left or not presents:
            break
    way = input()

if not presents and nice_kids_left:
    print("Santa ran out of presents!")

[print(" ".join(row)) for row in hood]

if not nice_kids_left:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")