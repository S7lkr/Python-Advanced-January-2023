size = int(input())
matrix = [list(map(int, input().split(" "))) for _ in range(size)]
bombs_coordinates = [list(map(int, i.split(","))) for i in input().split(" ")]
cnt = 0
a_sum = 0

directions = (
    (-1, 0),    # up
    (1, 0),     # down
    (0, -1),    # left
    (0, 1),     # right
    (-1, -1),   # top-left
    (-1, 1),    # top-right
    (1, -1),    # bottom-left
    (1, 1),     # bottom-right
    (0, 0)      # current position (this should be last)
)

for r, c in bombs_coordinates:      # iterate through each bomb's coordinates
    bomb_power = matrix[r][c]       # bomb position
    if bomb_power <= 0:
        continue
    for x, y in directions:     # now we need to go in EVERY DIRECTION (bomb explode radius)
        if 0 <= r+x <= size-1 and 0 <= c+y <= size-1:     # check if all directions ARE INSIDE the matrix's size
            if matrix[r+x][c+y] <= 0:   # if any cell (around the bomb) is already 0 (dead)
                continue
            matrix[r+x][c+y] -= bomb_power      # after all checks the cell will be damaged from the explosion!
    matrix[r][c] = 0    # the bomb position itself becomes 0 (only after everything in its radius is destroyed)

for r in matrix:
    for el in r:
        if el > 0:
            cnt += 1    # active cell count
            a_sum += el     # sum of active cell values

print(f"Alive cells: {cnt}")
print(f"Sum: {a_sum}")
[print(*lst, sep=" ") for lst in matrix]