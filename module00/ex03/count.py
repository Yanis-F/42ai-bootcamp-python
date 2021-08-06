import string
import sys

def text_analyzer(text: str = None, *extra):
    """This function counts the number of upper characters, lower characters,punctuation and spaces in a given text"""

    if len(extra) > 0:
        print("ERROR", file=sys.stderr)
        return

    if text == None:
        text = input("What is the text to analyse?\n")

    length = len(text)
    upper_letter_count = sum(c in string.ascii_uppercase for c in text)
    lower_letter_count = sum(c in string.ascii_lowercase for c in text)
    ponctuation_mark_count = sum(c in string.punctuation for c in text)
    spaces_count = sum(c == ' ' for c in text)


    s_if_plural = lambda num : 's' if num != 1 else str()

    print(f"The text contains {length} character{s_if_plural(length)}:")
    print(f"- {upper_letter_count} upper letter{s_if_plural(upper_letter_count)}")
    print(f"- {lower_letter_count} lower letter{s_if_plural(lower_letter_count)}")
    print(f"- {ponctuation_mark_count} punctuation mark{s_if_plural(ponctuation_mark_count)}")
    print(f"- {spaces_count} space{s_if_plural(spaces_count)}")
