row, col = list(map(int, input().split(" ")))

matrix = [[''.join([chr(r+97), chr(c+97+r), chr(r+97)]) for c in range(col)] for r in range(row)]
[print(" ".join(row)) for row in matrix]