from collections import deque

colors = deque(input().split(" "))
main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}
collected_colors = []

while len(colors) > 1:
    first = colors.popleft()
    last = colors.pop() if colors else ""
    if first + last in main_colors or first + last in secondary_colors.keys():
        collected_colors.append(first + last)
    elif last + first in main_colors or last + first in secondary_colors.keys():
        collected_colors.append(last + first)
    else:
        if len(first) > 1:
            first = first[:-1]
            colors.insert(len(colors) // 2, first)
        if len(last) > 1:
            last = last[:-1]
            colors.insert(len(colors) // 2, last)
else:
    if colors and colors[0] in main_colors:
        collected_colors.append(colors.pop())

for color in collected_colors:
    if color in secondary_colors.keys() and not secondary_colors[color].issubset(collected_colors):
        collected_colors.remove(color)

print(collected_colors)