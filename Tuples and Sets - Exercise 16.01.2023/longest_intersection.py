list_ranges = [[list(map(int, r.split(","))) for r in input().split("-")] for _ in range(int(input()))]
set_ranges = [set() for _ in range(len(list_ranges) * 2)]
intersections = []

index = 0
for lst in list_ranges:
    for lst2 in lst:
        for digit in range(lst2[0], lst2[1] + 1):
            set_ranges[index].add(digit)
        index += 1

for idx in range(0, len(set_ranges), 2):
    intersect = set_ranges[idx].intersection(set_ranges[idx + 1])
    intersections.append(intersect)

lens = [len(lst) for lst in intersections]
longest = lens.index(max(lens))
print(f"Longest intersection is {list(intersections[longest])} with length {max(lens)}")
