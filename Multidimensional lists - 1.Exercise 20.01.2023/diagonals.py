size = int(input())
matrix = [list(map(int, input().split(", "))) for _ in range(size)]

diagonal1 = [matrix[i][i] for i in range(size)]     # diagonal "\"
# With "enumerate" -> [r] will increase by 1 and [c] will decrease by 1 on each iteration
diagonal2 = [matrix[r][c] for r, c in enumerate(range(size-1, -1, -1))]     # diagonal "/"

sum_of_primary = sum(diagonal1)
sum_of_secondary = sum(diagonal2)

print(f"Primary diagonal: {', '.join(list(map(str, diagonal1)))}. Sum: {sum_of_primary}")
print(f"Secondary diagonal: {', '.join(list(map(str, diagonal2)))}. Sum: {sum_of_secondary}")

# d2 = m[0][2], m[1][1], m[2][0] -> size 3
# d2 = m[0][3], m[1][2], m[2][1], m[3][0] -> size 4