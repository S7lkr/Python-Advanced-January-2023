import sys

r_c = list(map(int, input().split(" ")))
rows = r_c[0]
cols = r_c[1]
matrix = [list(map(int, input().split(" "))) for _ in range(rows)]
max_sum = -sys.maxsize
cur_sum = 0
max_matrix = []
cur_matrix = []

for r in range(rows-2):
    for c in range(cols-2):
        row1 = matrix[r][c:c+3]
        row2 = matrix[r+1][c:c+3]
        row3 = matrix[r+2][c:c+3]
        cur_matrix = [row1, row2, row3]
        cur_sum = sum([sum(r) for r in cur_matrix])
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_matrix = cur_matrix

print(f"Sum = {max_sum}")
[print(*r, sep=" ") for r in max_matrix]