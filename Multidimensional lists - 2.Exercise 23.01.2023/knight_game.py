from sys import maxsize

n = int(input())
board = [list(input()) for _ in range(n)]

moves = (
    (-2, -1),   # uul
    (-2, 1),    # uur
    (2, -1),    # ddl
    (2, 1),     # ddr
    (-1, -2),   # llu
    (1, -2),    # lld
    (-1, 2),    # rru
    (1, 2),     # rrd
)
removed_knights = 0

while True:
    max_attacks = 0
    knight_max_attacks_pos = []

    for r in range(n):
        for c in range(n):
            if board[r][c] == "K":
                attacks = 0
                for x, y in moves:
                    if 0 <= r+x < n and 0 <= c+y < n:   # valid coordinates
                        if board[r+x][c+y] == "K":
                            attacks += 1
                if attacks > max_attacks:
                    knight_max_attacks_pos = [r, c]
                    max_attacks = attacks

    if knight_max_attacks_pos:      # if there is EVEN ONE horse that can attack others:
        a, b = knight_max_attacks_pos
        board[a][b] = "0"
        removed_knights += 1
    else:
        break
print(removed_knights)