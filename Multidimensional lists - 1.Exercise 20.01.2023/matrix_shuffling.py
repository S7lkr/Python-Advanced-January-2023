def data_validator(command, data):
    data = [idx for idx in data if int(idx) < rows or int(idx) < cols]
    if len(data) != 4 or command != "swap":
        return False
    return True


rows, cols = list(map(int, input().split(" ")))
matrix = [input().split(" ") for _ in range(rows)]

act, *info = input().split(" ")

while act != "END" or act == "swap":
    if not data_validator(act, info):
        print("Invalid input!")
        act, *info = input().split(" ")
        continue
    r1, c1, r2, c2 = [int(x) for x in info]
    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
    [print(*r, sep=" ") for r in matrix]
    act, *info = input().split(" ")