field_size = int(input())   # NOTE: only in square matrices we don't need rows and cols number
r = c = field_size
commands = input().split(" ")
field = [input().split(" ") for _ in range(field_size)]
coal_left = sum([sum([1 for ch in r if ch == "c"]) for r in field])
coal_gain = 0
exit_reached = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for row in range(field_size):
    for col in range(field_size):
        if field[row][col] == "s":
            r, c = row, col

for command in commands:
    x, y = directions[command]      # which direction to move
    r, c = r+x, c+y     # after each move we WILL STAY on that NEW position
    if r < 0 or r >= field_size or c < 0 or c >= field_size:  # check for invalid 'r' or 'c'
        r, c = r-x, c-y
        continue
    if field[r][c] == "e":  # if we step onto "e":
        exit_reached = True
        print(f"Game over! ({r}, {c})")
        break
    elif field[r][c] == "c":
        coal_gain += 1
        coal_left -= 1
    field[r][c] = "s"
    field[r-x][c-y] = "*"
    if not coal_left:
        print(f"You collected all coal! ({r}, {c})")
        break
else:
    if not exit_reached and coal_left:
        print(f"{coal_left} pieces of coal left. ({r}, {c})")