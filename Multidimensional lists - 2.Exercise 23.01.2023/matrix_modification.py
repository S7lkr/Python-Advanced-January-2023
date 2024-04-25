def add_func(lst):
    r, c, value = lst
    if 0 <= r < n and 0 <= c < n:
        matrix[r][c] += value
    else:
        print("Invalid coordinates")


def subtract_func(lst):
    r, c, value = lst
    if 0 <= r < n and 0 <= c < n:
        matrix[r][c] -= value
    else:
        print("Invalid coordinates")


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

while True:
    line = input().split(" ")
    if line[0] == "END":
        break
    act = line.pop(0)
    line = list(map(int, line))
    if act == "Add":
        add_func(line)
    elif act == "Subtract":
        subtract_func(line)

[print(*lst, sep=" ") for lst in matrix]