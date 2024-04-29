def words_sorting(*args):
    words_sum = {}
    for word in args:
        words_sum[word] = 0
        for ch in word:
            words_sum[word] += ord(ch)
    if sum(words_sum.values()) % 2 == 0:
        words_sum = [f"{w} - {num}" for w, num in sorted(words_sum.items(), key=lambda x: x[0])]
        return "\n".join(words_sum)
    words_sum = [f"{w} - {num}" for w, num in sorted(words_sum.items(), key=lambda x: -x[1])]
    return "\n".join(words_sum)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology')
)