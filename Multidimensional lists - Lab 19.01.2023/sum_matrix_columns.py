r_c = list(map(int, input().split(", ")))
rows = r_c[0]
cols = r_c[1]
matrix = [[int(x) for x in input().split(" ")] for _ in range(rows)]
summed_columns = [[] for c in range(cols)]

# REMEMBER: to through every ROW: 1st loop is in range ROWS. For COLUMNS is vice versa.
# We need to go through EVERY COLUMN
for row in range(cols):     # 5 cols (5 iterations)                 [0, 1, 2, 3, 4]
    for col in range(rows):     # 2 rows in each iteration          [5, 6, 7, 8, 9]
        summed_columns[row].append(matrix[col][row]) # #             |           |
    summed_columns[row] = sum(summed_columns[row])  # #              V           V
print(*summed_columns, sep="\n")    # #                            [0,5]...    [4,9]
