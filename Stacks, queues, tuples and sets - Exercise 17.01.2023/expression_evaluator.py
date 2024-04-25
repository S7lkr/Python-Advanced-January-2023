from functools import reduce

expression = input().split(" ")
idx = 0

# reduce(val1, (+, >=,...), val2, (array)) -> repeats an operation between first two elements in iterable and stores
# back the result ON THE SAME POSITION of the first two. Repeats UNTIL there is ONLY ONE value left
functions = {
    "+": lambda i: reduce(lambda a, b: a + b, expression[:i]),  # sum 1st 2 elmnts, until 1 elmnt is left
    "-": lambda i: reduce(lambda a, b: a - b, expression[:i]),
    "*": lambda i: reduce(lambda a, b: a * b, expression[:i]),
    "/": lambda i: reduce(lambda a, b: a / b, expression[:i]),
}

while idx < len(expression):    # after each operation we remove elements -> len decreases: idx = 2, exp["2", "3", "+"]
    element = expression[idx]   # so exp[2] is THE LAST possible index. When index becomes 3, while-loop ends!
    if element in "+-*/":
        expression[:idx] = map(int, expression[:idx])
        result = functions[element](idx)
        [expression.pop(1) for _ in range(idx)]
        expression[0] = result
        idx = 0
    idx += 1

print(int(expression[0]))