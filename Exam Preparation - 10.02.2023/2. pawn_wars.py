from collections import deque


def queen_check(wh_pos, bl_pos):
    if wh_pos[0] < (7 - bl_pos[0]):     # if white pawn has LESS rows to the top from the black pawn
        return f"Game over! White pawn is promoted to a queen at {columns[wh_pos[1]]}8."    # white becomes queen
    return f"Game over! Black pawn is promoted to a queen at {columns[bl_pos[1]]}1."        # else, black becomes queen


def locate_players():   # this func locates the coordinates of the white and black pawns before start of game
    wh_pos = 0
    bl_pos = 0
    row_ind = 0
    for row in board:
        if "w" in row:
            wh_pos = (row_ind, row.index("w"))
        if "b" in row:
            bl_pos = (row_ind, row.index("b"))
        row_ind += 1
    return wh_pos, bl_pos


board = [input().split(" ") for _ in range(8)]
rows = "87654321"       # register ROWS and COLUMNS of the chess board
columns = "abcdefgh"
capture = False

white_pos, black_pos = locate_players()             # get the white and black pawns' locations
player_positions = deque([white_pos, black_pos])    # save both tuples into a deque
pawn_turn, pawn_wait = ["w", "b"]               # white moves UP, black moves DOWN by 1 square
players = ["White", "Black"]
way = [-1, 1]                   # movement direction (UP, DOWN) will change on every turn
captured_pos = (0, 0)

while not capture:
    if abs(white_pos[1] - black_pos[1]) > 1:       # if the columns of the two positioned pawns are next to each other:
        print(queen_check(white_pos, black_pos))   # check which pawn will become queen first, and win
        queen = True
        break
    pl_turn = player_positions.popleft()    # take the coordinates of the pawn's turn
    r, c = pl_turn                          # shorten and simplify the code -> r, c = pl_turn[0], pl_turn[1]
    board[r][c] = "-"
    r += way[0]                         # change ROW index (up or down)
    board[r][c] = pawn_turn[0]          # cell, which pawn has moved on (taken cell)

    # Capture condition -> AFTER MOVE, if played pawn is on same row with the other and in neighbour columns:
    if r == player_positions[0][0] and abs(c - player_positions[0][1]) == 1:
        captured_pos = player_positions[0][0], player_positions[0][1]   # save the captured pawn coordinates
        capture = True
        continue
    # NEXT PLAYER'S TURN:
    player_positions.append((r, c))                 # the played pawn's postion goes at the end of the players deque
    pawn_turn, pawn_wait = pawn_wait, pawn_turn     # swap "w" <-> "b"
    players[0], players[1] = players[1], players[0]     # these are for the prints
    way[0], way[1] = way[1], way[0]                 # change move direction UP <-> DOWN

if capture:
    print(f"Game over! {players[0]} win, capture on {columns[captured_pos[1]]}{rows[captured_pos[0]]}.")