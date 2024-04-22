import string

with open("input.txt", "w") as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n"
               "-Is this some kind of joke?! Is it?\n"
               "-Quick, hide here. It is safer.")

punctuation = (",", ".", "-")

with open("input.txt", "r") as file:
    all_lines = file.readlines()

    with open("output.txt", "w") as file2:
        for line in range(len(all_lines)):
            letters_cnt = 0
            symbol_cnt = 0

            for ch in all_lines[line]:
                if ch.isalpha():
                    letters_cnt += 1
                elif ch in string.punctuation:
                    symbol_cnt += 1

            all_lines[line] = all_lines[line].replace("\n", "")
            print(all_lines[line])
            file2.write(f"Line {line + 1}: {all_lines[line]} ({letters_cnt})({symbol_cnt})\n")