text = list(input())
a_stack = []

for idx in range(len(text)):
    if text[idx] == "(":
        a_stack.append(idx)
    elif text[idx] == ")":
        last_opened_bracket = a_stack.pop()
        print("".join(text[last_opened_bracket:idx + 1]))