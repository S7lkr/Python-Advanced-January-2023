try:
    text = input()
    times = int(input())
    result = text * times
    print(result)
except ValueError:
    print("Variable times must be an integer")