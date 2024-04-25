size = int(input())
matrix = [list(map(int, input().split(" "))) for _ in range(size)]

diagonal1 = [matrix[i][i] for i in range(size)]     # diagonal "\"
diagonal2 = [matrix[r][c] for r, c in enumerate(range(size-1, -1, -1))]     # diagonal "/"

sum_of_primary = sum(diagonal1)
sum_of_secondary = sum(diagonal2)

result = abs(sum_of_primary - sum_of_secondary)
print(result)