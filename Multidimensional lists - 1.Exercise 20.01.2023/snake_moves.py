from collections import deque

rows, cols = list(map(int, input().split(" ")))
word = list(input())    # word as list -> ['d', 'o', 'g']
word_copy = deque(word)     # a 'copy' of the word, as a deque

# We will REMOVE THE FIRST 'NUMBER_OF_COLUMNS' elements in order to FILL the first row with them.
# After that, to what has remained of "word_copy" add the whole 'input_word' at the end
# Example: 2 rows, 3 cols, word = 'abc' -> the 1st row will be "ab". "c" is left, so we add "abc" behind it -> "cabc"
# We repeat the process until whole matrix is complete with enough rows and cols.

for row in range(rows):     # start FILLING the matrix. For EACH row:
    while len(word_copy) < cols:    # if "word_copy" is not enough to fill a row:
        word_copy.extend(word)      # extend THE WHOLE WORD at the end of "word_copy" -> "i"+"SoftUni" = "iSoftUni"
    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(cols)], sep="")  # it will remove and print each 1st element
    else:                                                           # for 'NUMBER OF COLS' times
        print(*[word_copy.popleft() for _ in range(cols)][::-1], sep="")    # same, but REVERSE the list before print