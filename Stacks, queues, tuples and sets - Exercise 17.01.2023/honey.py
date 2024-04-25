from collections import deque

bees = deque(list(map(int, input().split(" "))))
nectar_amount = list(map(int, input().split(" ")))
operations = deque(input().split(" "))
honey_made = 0

functions = {
    "+": lambda a, b: abs(a + b),
    "-": lambda a, b: abs(a - b),
    "*": lambda a, b: abs(a * b),
    "/": lambda a, b: abs(a / b),
}

while bees and nectar_amount:
    bee = bees.popleft()
    nectar = nectar_amount.pop()
    if bee > nectar:
        bees.appendleft(bee)
    else:
        honey_made += functions[operations.popleft()](bee, nectar)

print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar_amount:
    print(f"Nectar left: {', '.join(map(str, nectar_amount))}")