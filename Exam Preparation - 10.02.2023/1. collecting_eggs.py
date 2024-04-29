from collections import deque

eggs = deque(input().split(", "))
papers = input().split(", ")
boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    egg = int(egg)
    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    if egg <= 0:
        continue
    paper = papers.pop()
    if egg + int(paper) <= 50:
        boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(papers)}")