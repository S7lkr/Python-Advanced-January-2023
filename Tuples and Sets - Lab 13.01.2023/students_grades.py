students = [input().split(" ") for _ in range(int(input()))]
students_data = {}

for st in students:
    person, grade = st
    if person not in students_data.keys():
        students_data[person] = []
    students_data[person].append(float(grade))

for p, gr in students_data.items():
    print(p, end=" -> ")
    for g in gr:
        print(f"{g:.2f}", end=" ")
    print(f"(avg: {sum(gr) / len(gr):.2f})")

# [print(f"{p} -> {' '.join(gr)} (avg:{sum(gr) / len(gr):.2f})") for p, gr in students_data.items()]