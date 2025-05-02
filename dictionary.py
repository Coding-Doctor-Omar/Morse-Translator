DASH = "-"
DOT = "."
SPACE = "/"

numbers = {
    "0": DASH * 5,
    "1": DOT + DASH * 4,
    "2": DOT * 2 + DASH * 3,
    "3": DOT * 3 + DASH * 2,
    "4": DOT * 4 + DASH,
    "5": DOT * 5,
    "6": DASH + DOT * 4,
    "7": DASH * 2 + DOT * 3,
    "8": DASH * 3 + DOT * 2,
    "9": DASH * 4 + DOT,
}

letters_and_symbols = {
    " ": SPACE,
    "a": DOT + DASH,
    "b": DASH + DOT * 3,
    "c": DASH + DOT + DASH + DOT,
    "d": DASH + DOT * 2,
    "e": DOT,
    "f": DOT * 2 + DASH + DOT,
    "g": DASH * 2 + DOT,
    "h": DOT * 4,
    "i": DOT * 2,
    "j": DOT + DASH * 3,
    "k": DASH + DOT + DASH,
    "l": DOT + DASH + DOT * 2,
    "m": DASH * 2,
    "n": DASH + DOT,
    "o": DASH * 3,
    "p": DOT + DASH * 2 + DOT,
    "q": DASH * 2 + DOT + DASH,
    "r": DOT + DASH + DOT,
    "s": DOT * 3,
    "t": DASH,
    "u": DOT * 2 + DASH,
    "v": DOT * 3 + DASH,
    "w": DOT + DASH * 2,
    "x": DASH + DOT * 2 + DASH,
    "y": DASH + DOT + DASH * 2,
    "z": DASH * 2 + DOT * 2,
    ".": DOT + DASH + DOT + DASH + DOT + DASH,
    ",": DASH * 2 + DOT * 2 + DASH * 2,
    "?": DOT * 2 + DASH * 2 + DOT * 2,
    "'": DOT + DASH * 4 + DOT,
    "!": DASH + DOT + DASH + DOT + DASH * 2,
    "/": DASH + DOT * 2 + DASH + DOT,
    "&": DOT + DASH + DOT * 3,
    ":": DASH * 3 + DOT * 3,
    ";": DASH + DOT + DASH + DOT + DASH + DOT,
    "=": DASH + DOT * 3 + DASH,
    "+": DOT + DASH + DOT + DASH + DOT,
    "-": DASH + DOT * 4 + DASH,
    "_": DOT * 2 + DASH * 2 + DOT + DASH,
    '"': DOT + DASH + DOT * 2 + DASH + DOT,
    "$": DOT * 3 + DASH + DOT * 2 + DASH,
    "@": DOT + DASH * 2 + DOT + DASH + DOT,
}

letters_and_symbols_values = [value for value in letters_and_symbols.values()]
letters_and_symbols_keys = [key for key in letters_and_symbols.keys()]
numbers_values = [value for value in numbers.values()]
numbers_keys = [key for key in numbers.keys()]

morse = {}

for value in letters_and_symbols_values:
    key = ""

    for item in letters_and_symbols:
        if letters_and_symbols[item] == value:
            key = item
            break

    morse.update({value: key})

for value in numbers_values:
    key = ""

    for item in numbers:
        if numbers[item] == value:
            key = item
            break

    morse.update({value: key})

morse.update({" ": ""})

def translate(string, to="morse"):
    """Translates the text or morse. The 'string' parameter is the user input,
    while the 'to' parameter is the method of translation (defaults to 'morse')."""

    if to == "morse":
        translation_chars = []

        for char in string:
            if char in letters_and_symbols:
                translation_chars.append(" " + letters_and_symbols[char])
            elif char in numbers:
                translation_chars.append(" " + numbers[char])
            else:
                return None

        translation = " ".join(translation_chars)
        return translation

    elif to == "text":
        string_words = string.strip().split(" / ")
        translation_words = []

        for word in string_words:
                translated_word = ""
                word_chars = word.split(" ")

                for char in word_chars:
                    if char in morse:
                        translated_word += morse[char]
                    else:
                        return None

                translation_words.append(translated_word)


        translation = ""

        for word in translation_words:
            translation += word + " "

        return translation

    raise ValueError("Invalid 'to' argument. Expected 'text' or 'morse'.")

