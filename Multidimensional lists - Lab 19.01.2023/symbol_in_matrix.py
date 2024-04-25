size = int(input())
matrix = [list(input()) for _ in range(size)]
symbol = input()
symbol_found = False

for row in range(size):
    if symbol_found:
        break
    for col in range(size):
        ch = matrix[row][col]
        if ch == symbol:
            print((row, col))
            symbol_found = True
            break
if not symbol_found:
    print(f"{symbol} does not occur in the matrix")