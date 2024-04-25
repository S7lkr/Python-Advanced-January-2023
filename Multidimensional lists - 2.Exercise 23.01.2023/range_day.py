def move(way, steps):
    r = shooter_pos[0] + (directions[way][0] * steps)
    c = shooter_pos[1] + (directions[way][1] * steps)
    if not (0 <= r < 5 and 0 <= c < 5):
        return shooter_pos
    if sh_range[r][c] == "x":
        return shooter_pos
    return [r, c]


def shoot(way):
    r, c = shooter_pos      # current shooter position
    x, y = directions[way]  # given direction (1, 0)
    r += x
    c += y
    while 0 <= r < 5 and 0 <= c < 5:
        if sh_range[r][c] == "x":
            sh_range[r][c] = "."
            return [r, c]
        r += x
        c += y


sh_range = [input().split(" ") for _ in range(5)]
targets = 0
targets_hit_pos = []
shooter_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for a in range(5):
    for b in range(5):
        if sh_range[a][b] == "x":
            targets += 1
        elif sh_range[a][b] == "A":
            shooter_pos = [a, b]

targets_left = targets

for _ in range(int(input())):
    command = input().split(" ")
    act = command[0]
    direction = command[1]
    if act == "move":
        distance = int(command[2])
        shooter_pos = move(direction, distance)
    elif act == "shoot":
        result = shoot(direction)
        if result:
            targets_hit_pos.append(result)
            targets_left -= 1
    if not targets_left:    # if targets_left == O:
        print(f"Training completed! All {targets} targets hit.")
        break
else:
    print(f"Training not completed! {targets_left} targets left.")

print(*targets_hit_pos, sep="\n")