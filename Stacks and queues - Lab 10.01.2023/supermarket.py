from collections import deque

client = input()
a_deque = deque()

while client != "End":
    if client == "Paid":
        while a_deque:
            print(a_deque.popleft())
    else:
        a_deque.append(client)
    client = input()
else:
    print(f"{len(a_deque)} people remaining.")