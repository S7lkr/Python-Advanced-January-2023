set1 = set(list(map(int, input().split(" "))))
set2 = set(list(map(int, input().split(" "))))

functions = {
    "Add First": lambda x: [set1.add(el) for el in x],
    "Add Second": lambda x: [set2.add(el) for el in x],
    "Remove First": lambda x: [set1.discard(el) for el in x],
    "Remove Second": lambda x: [set2.discard(el) for el in x],
    "Check Subset": lambda: print(set1.issubset(set2) or set1.issuperset(set2))
}

for _ in range(int(input())):
    first_act, *nums = input().split(" ")    # command = Add, *nums = "First", "5", "6"
    act = first_act + " " + nums.pop(0)

    # NOTE: Now with lambdas, we DO NOT NEED to make if-else checks!!!
    if nums:
        nums = list(map(int, nums))
        functions[act](nums)
    else:
        functions["Check Subset"]()

print(*sorted(set1), sep=", ")
print(*sorted(set2), sep=", ")