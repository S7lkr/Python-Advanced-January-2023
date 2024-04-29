from collections import deque

ramen_bowls = list(map(int, input().split(", ")))
customers = deque(list(map(int, input().split(", "))))

while ramen_bowls and customers:
    bowl = ramen_bowls.pop()
    cust = customers.popleft()
    if bowl > cust:
        ramen_bowls.append(bowl - cust) if bowl-cust != 0 else None
    else:
        customers.appendleft(cust - bowl) if cust - bowl != 0 else None
else:
    if not customers:
        print("Great job! You served all the customers.")
    else:
        print("Out of ramen! You didn't manage to serve all customers.")

if customers:
    print(f"Customers left: {', '.join(list(map(str, customers)))}")

if ramen_bowls:
    print(f"Bowls of ramen left: {', '.join(list(map(str, ramen_bowls)))}")