symbols_to_replace = ("-", ",", ".", "!", "?")

with open("input.txt", "w") as file:   # we enter the input text
    file.write(
        "-I was quick to judge him, but it wasn't his fault.\n-Is this some kind of joke?! Is it?\n"
        "-Quick, hide here. It is safer."
    )
with open("input.txt", "r") as file:   # open file "even_lines.txt" for READ. Open a beer also :)
    lines = file.readlines()    # represent all the lines in the file as a list
    even_lines = []     # here we will store the EVEN lines. And edit them later

    for i in range(len(lines)):     # iterate every line
        if i % 2 == 0:      # if line is on EVEN position:

            for ch in lines[i]:             # iterate every SYMBOL in that line
                if ch in symbols_to_replace:        # if current symbol is one of the symbols in line1 of code:
                    lines[i] = lines[i].replace(ch, "@")    # replace it with "@" dude

            lines[i] = lines[i].replace("\n", "")       # get rid of the GOD DAMN "\n"-symbols. Ouu yeah!
            even_lines.append(lines[i])         # now line is ready to be added to the list "even_lines"

with open("output.txt", "w") as file2:  # now open for WRITING. Open second beer!
    for line in even_lines:     # now iterate through THE EDITED lines
        result = reversed(line.split(" "))   # make EVERY line into a reversed list
        file2.write(" ".join(result))
        file2.write("\n")