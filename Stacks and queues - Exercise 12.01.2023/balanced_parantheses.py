from collections import deque

parentheses = deque(input())
opened_brackets = []

while parentheses:      # until THERE ARE ELEMENTS in deque "parentheses":
    if parentheses[0] in "([{":     # check if element is an OPENED BRACKET:
        opened_brackets.append(parentheses.popleft())   # REMOVE it from "parenthesis" and add it to "opened_brackets"
    elif not opened_brackets:   # if there are not ANY OPEN BRACKETS at all, BREAK
        print("NO")
        break
    else:
        if f"{opened_brackets.pop() + parentheses.popleft()}" not in "()[]{}": # if last_opened bracket doesn't match
            print("NO")                                                        # with the first_closed, BREAK
            break
else:   # when we come to the point, where "parenthesis" is EMPTY, that means everything went smooth!
    print("YES")