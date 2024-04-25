rows, cols = list(map(int, input().split(" ")))
bunny_lair = [list(input()) for _ in range(rows)]
commands = list(input())

dead = False
escaped = False
win = ()
lose = ()
r, c = 0, 0  # player current position will be stored here

directions = {
    "U": (-1, 0),  # up
    "D": (1, 0),  # down
    "L": (0, -1),  # left
    "R": (0, 1),  # right
}
cloned_bunnies = []
cloned_cells = []

for curr_row in range(rows):
    if "P" in bunny_lair[curr_row]:  # search through every row
        curr_col = bunny_lair[curr_row].index("P")  # when row found, get the index of "P"
        r, c = curr_row, curr_col  # player's starting position found

for move in commands:
    if dead:
        break
    x, y = directions[move]  # the name of the move "U" is the value of the corresponding direction key -> up (-1,0)
    if r + x < 0 or rows <= r + x or c + y < 0 or cols <= c + y:  # if R or C are OUTSIDE the matrix, player escapes!
        bunny_lair[r][c] = "."
        win = r, c
        escaped = True
    else:
        r, c = r + x, c + y
        new_pos = bunny_lair[r][c]  # the position after a move
        if new_pos == "B":  # if player steps on a BUNNY, he DIES
            bunny_lair[r-x][c-y] = "."
            lose = r, c
            dead = True
        else:  # otherwise (steps on ".") everything is fine, and he goes on
            bunny_lair[r][c] = "P"  # player "occupies" the new cell
            bunny_lair[r - x][c - y] = "."  # the cell, on which player WAS, is freed -> "."

    # after player finishes his move, it is bunnies turn (to clone)
    for r_ in range(rows):
        for c_ in range(cols):
            # first bunny found will clone (and will be stored as a CLONED BUNNY)
            # next found bunny will clone ONLY IF it was not already cloned
            if bunny_lair[r_][c_] == "B" and (r_, c_) not in cloned_cells and (r_, c_) not in cloned_bunnies:
                cloned_bunnies.append((r_, c_))
                for x_, y_ in directions.values():  # clone in every direction
                    if r_ + x_ < 0 or rows <= r_ + x_ or c_ + y_ < 0 or cols <= c_ + y_:
                        continue
                    if bunny_lair[r_ + x_][c_ + y_] == "P":
                        dead = True
                        lose = r, c
                    bunny_lair[r_ + x_][c_ + y_] = "B"
                    cloned_cells.append((r_ + x_, c_ + y_))
    else:
        cloned_cells.clear()
    if escaped or dead:
        break

[print(*lst, sep="") for lst in bunny_lair]
if escaped:
    print(f"won: {win[0]} {win[1]}")
elif dead:
    print(f"dead: {lose[0]} {lose[1]}")