text = list(input())
occurrences = {ch: text.count(ch) for ch in text}

[print(f"{k}: {v} time/s") for k, v in sorted(occurrences.items())]