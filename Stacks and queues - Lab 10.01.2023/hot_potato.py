from collections import deque

names = input().split(" ")
n = int(input())
players_out = deque()
idx = 0

while names:
    cnt = n + idx
    while cnt > len(names):
        cnt -= len(names)
    idx = cnt - 1
    players_out.append(names.pop(idx))
    if idx > len(names) - 1:
        idx = 0

while len(players_out) > 1:
    print(f"Removed {players_out.popleft()}")
else:
    print(f"Last is {players_out.popleft()}")