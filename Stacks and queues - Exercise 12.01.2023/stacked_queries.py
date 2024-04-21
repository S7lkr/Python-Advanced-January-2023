numbers = []

functions = {       # we create a dictionary
    1: lambda x: numbers.append(x[1]),      # in which THE KEYS are the possible commands -> 1, 2, 3 or 4
    2: lambda x: numbers.pop() if numbers else None,    # NOTE: every lambda func is a VALUE !!
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None,
}
for _ in range(int(input())):
    command = [int(i) for i in input().split()]     # we cast everything in the command into INT-s -> [1, 20]
    functions[command[0]](command)      # we CALL the lambda funcs via the keys in the dict

print(*reversed(numbers), sep=", ")


# a_stack = []
#
# for _ in range(int(input())):
#     command = input().split()
#     act = command[0]
#     if act == "1":
#         a_stack.append(int(command[1]))
#     elif act == "2" and a_stack:
#         a_stack.pop()
#     elif act == "3" and a_stack:
#         print(max(a_stack))
#     elif act == "4" and a_stack:
#         print(min(a_stack))
#
# print(*reversed(a_stack), sep=", ")