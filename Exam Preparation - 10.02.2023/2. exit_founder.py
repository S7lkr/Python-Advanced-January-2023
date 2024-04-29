from collections import deque


def player_change():
    tom_jerry[0], tom_jerry[1] = tom_jerry[1], tom_jerry[0]


tom_jerry = deque(input().split(", "))
board = [input().split(" ") for _ in range(6)]

stunned = []
command = input()

while command:
    player, player_wait = tom_jerry
    if player in stunned:
        stunned.remove(player)
        player_change()
        command = input()
        continue
    command = command.strip("()").split(", ")
    command = list(map(int, command))
    r, c = command

    if board[r][c] == "E":
        print(f"{player} found the Exit and wins the game!")
        break
    elif board[r][c] == "T":
        print(f"{player} is out of the game! The winner is {player_wait}.")
        break
    elif board[r][c] == "W":
        stunned.append(player)
        print(f"{player} hits a wall and needs to rest.")

    player_change()
    command = input()