r_c = list(map(int, input().split(" ")))
rows = r_c[0]
cols = r_c[1]

matrix = [input().split(" ") for _ in range(rows)]
match = 0

for r in range(rows - 1):
    for c in range(cols - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            match += 1

print(match)