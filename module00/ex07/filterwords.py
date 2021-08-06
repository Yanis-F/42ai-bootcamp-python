from typing import List
import sys


def is_char_allowed_in_words(char):
    return char.isalnum() or char == '-' or char == '_'

def _filter_words(text: str, min_letter_count: int) -> List[str]:
    if min_letter_count <= 0:
        raise Exception("min_letter_count must be stricly positive")

    text = ''.join([c if is_char_allowed_in_words(c) else ' ' for c in text])
    words = text.split()

    return [w for w in words if len(w) > min_letter_count]


def filter_words(argv: List[str]) -> List[str]:
    if len(argv) != 3:
        raise Exception(
            "Expected exactly 2 arguments: <text> <min_letter_count>")

    return _filter_words(argv[1], int(argv[2]))

if __name__ == "__main__":
    try:
        print(filter_words(sys.argv))
    except Exception as e:
        print(str(e), file=sys.stderr)
        