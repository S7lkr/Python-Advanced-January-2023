size = int(input())
wonderland = [input().split(" ") for _ in range(size)]
r, c = 0, 0     # start
tea_bags = 0
failed = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for row in range(size):
    for col in range(size):
        if wonderland[row][col] == "A":
            r, c = row, col
            wonderland[r][c] = "*"
while tea_bags < 10:
    if failed:
        wonderland[r][c] = "*"
        break
    command = input()
    x = directions[command][0]
    y = directions[command][1]
    if r+x < 0 or size <= r+x or c+y < 0 or size <= c+y:
        failed = True
        break
    r, c = r+x, c+y
    if wonderland[r][c].isdigit():
        tea_bags += int(wonderland[r][c])
    elif wonderland[r][c] == "R":
        failed = True
    wonderland[r][c] = "*"
else:
    print("She did it! She went to the party.")

if failed:
    print("Alice didn't make it to the tea party.")

[print(" ".join(lst)) for lst in wonderland]