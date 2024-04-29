def add_songs(*data):
    result = []
    songs = {}

    for info in data:
        song, lyrics = info
        if song not in songs.keys():
            songs[song] = []
        songs[song].extend(lyrics)

    for s, l in songs.items():
        result.append(f"- {s}")
        if l:
            result.append("\n".join(l))
    result = "\n".join(result)
    return result


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))