import sys
from typing import List

def odd_even_or_zero(argv: List[str]) -> str:
    number: int

    try:
        if len(argv) != 2:
            raise Exception()
        number = int(argv[1])
    except Exception:
        return "ERROR"

    if number == 0:
        return "I'm Zero."
    if number % 2:
        return "I'm Odd."
    else:
        return "I'm Even."


if __name__ == '__main__':
    print(odd_even_or_zero(sys.argv))
