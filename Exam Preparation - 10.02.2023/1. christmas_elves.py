from collections import deque

elves = deque(list(map(int, input().split())))
boxes = list(map(int, input().split()))

total_energy = 0
toys = 0

made_toy = False
made_2_toys = False

day = 1
while elves and boxes:
    made_toy = False
    made_2_toys = False
    elf = elves.popleft()
    if elf < 5:             # if elf's energy is less than 5, JUST remove the elf and continue operations
        continue
    box = boxes.pop()
    if elf >= box:                                  # if elf has energy to make a toy:
        if day % 3 == 0:                            # if day is: 3, 6, 9, 12....etc.
            if elf >= box * 2:                          # then he requires DOUBLE energy
                elves.append((elf - box * 2) + 1)       # elf eats cookie -> +1
                made_2_toys = True
                toys += 2
                total_energy += box * 2             # DOUBLE energy spent
            else:                                   # if elf doesn't have energy for DOUBLE work:
                elves.append(elf * 2)               # eats chocolate and goes at the end of elves deque
                boxes.append(box)                   # box returned on its place
        else:   # ordinary day (NOT 3, 6, 9, 12, 15, etc.)
            elves.append(elf - box + 1)             # eat cookie
            made_toy = True
            toys += 1
            total_energy += box                     # energy spent
    else:
        elves.append(elf * 2)                       # eat chocolate
        boxes.append(box)                           # return box
    if day % 5 == 0:            # every 5, 10, 15, etc....day
        if made_toy:            # if a toy is made
            toys -= 1
            elves[-1] -= 1      # elf won't eat cookie
        elif made_2_toys:       # if 2 toys made
            toys -= 2
            elves[-1] -= 1
    day += 1                    # increase DAY on every iteration

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")

if elves:
    print(f"Elves left: {', '.join(list(map(str, elves)))}")
if boxes:
    print(f"Boxes left: {', '.join(list(map(str, boxes)))}")