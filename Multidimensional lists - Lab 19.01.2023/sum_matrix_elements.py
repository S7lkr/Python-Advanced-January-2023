r_c = list(map(int, input().split(", ")))  # [3, 6]
rows = r_c[0]
cols = r_c[1]
matrix = [list(map(int, input().split(", "))) for _ in range(rows)]

print(sum([sum(x) for x in matrix]))
print(matrix)