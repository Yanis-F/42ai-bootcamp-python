import sys
from typing import List


def reverse_and_swap_case(strings: List[str]) -> str:
    concact = ' '.join(strings)
    return concact[::-1].swapcase()



if __name__ == '__main__':
    print(reverse_and_swap_case(sys.argv[1:]))
