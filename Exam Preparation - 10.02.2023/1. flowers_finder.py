from collections import deque


def word_check(v, c, fl):
    if v in fl:
        fl = fl.replace(v, "")
    if c in fl:
        fl = fl.replace(c, "")
    return fl


flowers = ["rose", "tulip", "lotus", "daffodil"]
flowers_2 = flowers.copy()
found_word = False

vowels = deque(input().split(" "))
consonants = input().split(" ")

while vowels and consonants:
    vow = vowels.popleft()
    con = consonants.pop()
    ind = 0
    for flower in flowers_2:
        flowers_2[ind] = word_check(vow, con, flower)
        if flowers_2[ind] == "":
            found_word = True
            print(f"Word found: {flowers[ind]}")
        ind += 1
    if found_word:
        break


if not found_word:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")