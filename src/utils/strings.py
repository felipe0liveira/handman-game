import unicodedata


def normalize(word):
    return "".join(
        c
        for c in unicodedata.normalize("NFD", word.upper())
        if unicodedata.category(c) != "Mn"
    )
