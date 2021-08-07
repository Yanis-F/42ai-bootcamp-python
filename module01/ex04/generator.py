import random

def generator(text:str, sep: str=" ", option=None):
    if not text:
        return

    words = text.split(sep)

    if option == "shuffle":
        tmp = words
        words = []
        while tmp:
            idx = random.randint(0, len(tmp) - 1)
            words.append(tmp.pop(idx))
    elif option == "unique": 
        words = list(dict.fromkeys(words))
    elif option == "ordered":
        words = sorted(words)
    elif option is not None:
        raise Exception("Invalid option: '%s'" % option)

    for w in words:
        yield w
        