def car_move(a, b):
    global km_passed
    route[a][b] = "C"
    route[a-x][b-y] = "."
    km_passed += 10
    return route


size = int(input())
car_num = input()
route = [input().split(" ") for _ in range(size)]

r, c = 0, 0     # start rally position
route[0][0] = "C"
tunnels_pos = []
km_passed = 0
finished = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
row_cnt = 0
for row in route:
    if "T" in row:
        tunnels_pos.append((row_cnt, row.index("T")))
    row_cnt += 1

way = input()
while way != "End":
    x, y = directions[way]
    r, c = r + x, c + y
    if route[r][c] == "F":
        route = car_move(r, c)
        finished = True
        break
    elif route[r][c] == "T":
        route[r][c] = route[r-x][c-y] = "."
        tunnels_pos.remove((r, c))
        r, c = tunnels_pos[0]
        route[r][c] = "C"
        km_passed += 30
    else:
        route = car_move(r, c)
    way = input()
else:
    print(f"Racing car {car_num} DNF.")

if finished:
    print(f"Racing car {car_num} finished the stage!")

print(f"Distance covered {km_passed} km.")
[print("".join(line)) for line in route]