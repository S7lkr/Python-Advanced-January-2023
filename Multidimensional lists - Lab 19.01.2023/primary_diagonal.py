size = int(input())
matrix = [list(map(int, input().split(" "))) for _ in range(size)]

left_diagonal = [matrix[i][i] for i in range(size)]
print(sum(left_diagonal))