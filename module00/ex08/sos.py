import sys

MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}


def text2morse(text: str) -> str:
    if not all(char.isalnum() or char == " " for char in text):
        raise Exception("text must only contain alphanumeric characters")

    return " / ".join(' '.join([MORSE_CODE_DICT[char] for char in word]) for word in text.upper().split())


if __name__ == "__main__":
    try:
        print(text2morse(' '.join(sys.argv[1:])))
    except Exception as e:
        print(str(e), file=sys.stderr)
