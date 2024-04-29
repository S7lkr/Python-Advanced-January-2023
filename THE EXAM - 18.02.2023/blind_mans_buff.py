rows, cols = list(map(int, input().split(" ")))
matrix = [input().split(" ") for _ in range(rows)]

r, c = 0, 0
moves = 0
touched = 0
located = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for row in range(rows):
    if located:
        break
    for col in range(cols):
        if matrix[row][col] == "B":
            r, c = row, col
            located = True
            break

command = input()
while command != "Finish" and touched < 3:
    x, y = directions[command]
    if (0 <= r+x < rows and 0 <= c+y < cols) and matrix[r+x][c+y] != "O":
        r, c = r + x, c + y
        if matrix[r][c] == "P":
            touched += 1
        moves += 1
        matrix[r][c] = "B"
        matrix[r-x][c-y] = "-"

    command = input()
else:
    print("Game over!")

print(f"Touched opponents: {touched} Moves made: {moves}")