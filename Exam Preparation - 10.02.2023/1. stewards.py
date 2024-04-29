from collections import deque

seats = input().split(", ")
nums1 = deque(input().split(", "))
nums2 = deque(input().split(", "))

match_found = False
seat_matches = []
rotations = 0

while len(seat_matches) < 3 and rotations < 10:
    n1 = nums1.popleft()
    n2 = nums2.pop()
    letter = chr(int(n1) + int(n2))
    for seat in seats:
        if seat not in seat_matches:
            if f"{n1}{letter}" == seat or f"{n2}{letter}" == seat:
                match_found = True
                seat_matches.append(seat)
                break
    else:
        if not match_found:
            nums1.append(n1)
            nums2.appendleft(n2)
    match_found = False
    rotations += 1

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")