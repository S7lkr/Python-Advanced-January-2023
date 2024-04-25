rows = int(input())
flat_matrix = []
[flat_matrix.extend(input().split(", ")) for _ in range(rows)]
print(list(map(int, flat_matrix)))