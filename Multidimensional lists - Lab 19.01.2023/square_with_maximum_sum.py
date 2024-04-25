from sys import maxsize

rows, cols = list(map(int, input().split(", ")))
matrix = [list(map(int, input().split(", "))) for _ in range(rows)]

max_sum = -maxsize
current_sum = 0
max_matrix_2x2 = None
current_matrix = []

for r in range(rows - 1):
    for c in range(cols - 1):
        row1 = matrix[r][c:c+2]     # slice 1st row -> row[0:2] -> [matrix[0][0], matrix[0][1]]
        row2 = matrix[r+1][c:c+2]   # slice 2nd row -> row[1:2] -> [matrix[1][0], matrix[1][1]]
        current_matrix = [row1, row2]
        current_sum = sum([sum(r) for r in current_matrix])
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix_2x2 = current_matrix

[print(' '.join(list(map(str, r))), end="\n") for r in max_matrix_2x2]
print(max_sum)