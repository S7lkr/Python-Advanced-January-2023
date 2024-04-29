from collections import deque

foods = input().split(", ")
stamina = deque(input().split(", "))

mission_complete = False

peaks_data = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol":	100, "Polezhan": 60, "Kamenitza": 70}
peaks_conquered = []

while foods and stamina:
    food = foods.pop()
    energy = stamina.popleft()
    for key in peaks_data.keys():
        if int(food) + int(energy) >= peaks_data[key]:
            peaks_conquered.append(key)
            peaks_data.pop(key)
        break
    if not peaks_data:
        mission_complete = True
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
else:
    if not mission_complete:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if peaks_conquered:
    print("Conquered peaks:")
    [print(k) for k in peaks_conquered]