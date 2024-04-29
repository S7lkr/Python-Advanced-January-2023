from collections import deque

textiles = deque(list(map(int, input().split(" "))))
medicines = list(map(int, input().split(" ")))

healing_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicines:
    textile = textiles.popleft()
    med = medicines.pop()
    a_sum = textile + med
    if a_sum == 30:
        healing_items["Patch"] += 1
    elif a_sum == 40:
        healing_items["Bandage"] += 1
    elif a_sum == 100:
        healing_items["MedKit"] += 1
    elif a_sum > 100:
        healing_items["MedKit"] += 1
        medicines[-1] += (a_sum - 100)
    else:
        medicines.append(med + 10)

if not textiles and not medicines:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")

[print(f"{k} - {v}") for k, v in sorted(healing_items.items(), key=lambda x: (-x[1], x[0])) if v]

if medicines:
    print(f"Medicaments left: {', '.join([str(m) for m in reversed(medicines)])}")
if textiles:
    print(f"Textiles left: {', '.join([str(t) for t in reversed(sorted(textiles))])}")