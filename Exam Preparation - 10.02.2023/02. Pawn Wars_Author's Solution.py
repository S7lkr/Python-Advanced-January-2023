def check_if_can_capture(attacker_pos, defender_pos):
    att_row, att_col = attacker_pos
    def_row, def_col = defender_pos

    if att_row - 1 >= 0 and att_col - 1 >= 0:
        if att_row - 1 == def_row and att_col - 1 == def_col:
            return [att_row - 1, att_col - 1]
    if att_row - 1 >= 0 and att_col + 1 < 8:
        if att_row - 1 == def_row and att_col + 1 == def_col:
            return [att_row - 1, att_col + 1]
    if att_row + 1 < 8 and col - 1 >= 0:
        if att_row + 1 == def_row and att_col - 1 == def_col:
            return [att_row + 1, att_col - 1]
    if att_row + 1 < 8 and col + 1 < 8:
        if att_row + 1 == def_row and att_col + 1 == def_col:
            return [att_row + 1, att_col + 1]


matrix = []
for _ in range(8):
    matrix.append(input().split())

white_pos = []
black_pos = []

position_row = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}
positions_col = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

for row in range(8):
    for col in range(8):
        if matrix[row][col] == "w":
            white_pos = [row, col]
        if matrix[row][col] == "b":
            black_pos = [row, col]

for _ in range(8):
    capture_on = check_if_can_capture(white_pos, black_pos)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! White win, capture on {position}.")
        break

    white_pos[0] -= 1

    if white_pos[0] == 0:
        position = positions_col[white_pos[1]] + position_row[white_pos[0]]
        print(f"Game over! White pawn is promoted to a queen at {position}.")
        break

    capture_on = check_if_can_capture(black_pos, white_pos)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! Black win, capture on {position}.")
        break

    black_pos[0] += 1

    if black_pos[0] == 7:
        position = positions_col[black_pos[1]] + position_row[black_pos[0]]
        print(f"Game over! Black pawn is promoted to a queen at {position}.")
        break
