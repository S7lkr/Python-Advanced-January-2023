def result(even, odd):
    if sum(even) > sum(odd):
        return even.symmetric_difference(odd)
    elif sum(even) < sum(odd):
        return odd.difference(even)
    return even.union(odd)


n = int(input())
even_nums = set()
odd_nums = set()

names = [sum([ord(ch) for ch in list(input())]) // idx for idx in range(1, n+1)]
[even_nums.add(num) if num % 2 == 0 else odd_nums.add(num) for num in names]

print(", ".join(map(str, (result(even_nums, odd_nums)))))