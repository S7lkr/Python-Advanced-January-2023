def create(vl, *cl):
    k, l = cl
    if matrix[k][l] == ".":
        matrix[k][l] = vl
    return matrix


def update(vl, *cl):
    k, l = cl
    if matrix[k][l].isalnum():
        matrix[k][l] = vl
    return matrix


def delete(*cl):
    k, l = cl
    if matrix[k][l].isalnum():
        matrix[k][l] = "."
    return matrix


def read(*cl):
    k, l = cl
    if matrix[k][l].isalnum():
        return matrix[k][l]
    return False


def move(*args):
    a, b, d = args
    x, y = directions[d]
    a, b = a + x, b + y
    return a, b


size = 6
matrix = [input().split(" ") for _ in range(size)]
r, c = ((input().lstrip("(")).rstrip(")")).split(", ")
r, c = int(r), int(c)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
command = input()
while command != "Stop":
    act, *data = command.split(", ")
    way = data[0]
    cell = move(r, c, way)
    if act == "Create":
        val = data[1]
        matrix = create(val, *cell)
    elif act == "Update":
        val = data[1]
        matrix = update(val, *cell)
    elif act == "Delete":
        matrix = delete(*cell)
    elif act == "Read":
        if read(*cell):
            print(read(*cell))
    r, c = cell
    command = input()

[print(" ".join(row)) for row in matrix]