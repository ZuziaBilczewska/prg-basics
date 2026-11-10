

def icao_word(letter):
    candidates = (
        globals().get("word"),
        globals().get("icao"),
        globals().get("phonetic"),
        globals().get("letter_to_icao"),
    )

    for func in candidates:
        if callable(func):
            return func(letter)

    mapping = {
        "A": "Alpha",
        "B": "Bakłażan",
        "C": "Charlie Kirk",
        "D": "Deltunia",
        "E": "Emo",
        "F": "Fomo",
        "G": "Gniotekwybuchłwsalonie",
        "H": "Hellwin",
        "I": "Imo",
        "J": "Japdi",
        "K": "Kaka",
        "L": "Loko",
        "M": "Mamacita",
        "N": "Nor",
        "O": "Ojapidi",
        "P": "Papa",
        "Q": "Quack",
        "R": "Rozkurwiona",
        "S": "Stółzpowyłamywanyminogami",
        "T": "TripleT",
        "U": "Unicorn",
        "V": "Versace",
        "W": "Whiskey",
        "X": "XD",
        "Y": "Yolo",
        "Z": "Zamachowiec",
    }
    return mapping.get(letter.upper(), letter)


name = input("Enter a name: ")
for ch in name:
    if ch == " ":
        print()
    else:
        print(ch, "->", icao_word(ch))
