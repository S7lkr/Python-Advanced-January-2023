import re

file1 = open("words.txt", "w")
file2 = open("input.txt", "w")

file1.write("quick is fault")
file2.write("-I was quick to judge him, but it wasn't his fault.\n-Is this some kind of joke?! Is it?\n"
            "-Quick, hide here...It is safer.")

file1.close()
file2.close()

file1 = open("words.txt", "r")
file2 = open("input.txt", "r")
input_opened = file2.read()

word_counter = {}
words_lst = file1.read().split(" ")

for word in words_lst:
    word_counter[word] = 0
    pattern = fr"\b{word}\b"
    matches = re.findall(pattern, input_opened, flags=re.IGNORECASE)
    if matches:
        word_counter[word] += len(matches)
file1.close()
file2.close()

file3 = open("output.txt", "w")
result = [file3.write(f"{k} - {v}\n") for k, v in sorted(word_counter.items(), key=lambda x: -x[1])]

file3.close()
