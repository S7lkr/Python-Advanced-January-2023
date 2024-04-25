import sys

size = int(input())
field = [input().split(" ") for _ in range(size)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
bunny_start_pos = (0, 0)
max_eggs_on_path = -sys.maxsize
best_path = []
way = ""

for row in range(size):
    for col in range(size):
        if field[row][col] == "B":
            bunny_start_pos = (row, col)
            break

for k, v in directions.items():
    r, c = bunny_start_pos
    x, y = v
    eggs_on_path = 0
    curr_path = []
    while 0 <= r + x < size and 0 <= c + y < size:
        if field[r + x][c + y] == "X":
            break
        r, c = r+x, c+y
        eggs_on_path += int(field[r][c])
        curr_path.append([r, c])
    if eggs_on_path > max_eggs_on_path:
        max_eggs_on_path = eggs_on_path
        best_path = curr_path
        way = k

print(way)
print(*best_path, sep="\n")
print(max_eggs_on_path)