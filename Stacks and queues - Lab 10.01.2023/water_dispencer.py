from collections import deque

people = deque()
litres_in_disp = int(input())

while True:
    name = input()
    if name == "Start":
        break
    people.append(name)

command = input()
while command != "End":
    if "refill" in command:
        command = command.split(" ")
        litres_added = int(command[1])
        litres_in_disp += litres_added
    else:
        command = int(command)
        if command <= litres_in_disp:
            litres_in_disp -= command
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
    command = input()
print(f"{litres_in_disp} liters left")