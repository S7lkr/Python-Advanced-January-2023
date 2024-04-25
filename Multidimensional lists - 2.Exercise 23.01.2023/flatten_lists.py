matrix = [a.split() for a in input().split("|")]
print(*[" ".join(lst) for lst in reversed(matrix) if lst])