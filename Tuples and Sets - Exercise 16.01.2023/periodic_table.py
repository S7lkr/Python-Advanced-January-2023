lines = int(input())

unique_elements = set()
lists_of_elements = [[unique_elements.add(el) for el in input().split(" ")] for _ in range(lines)]
print("\n".join(sorted(unique_elements)))