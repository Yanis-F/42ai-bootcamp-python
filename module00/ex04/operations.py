import sys


def operations(a: int, b: int):
    if not (type(a) is int and type(b) is int):
        print("InputError: only numbers", file=sys.stderr)
        return

    sum = a + b
    diff = a - b
    product = a * b
    quotient = a / b if b != 0 else "ERROR (div by zero)"
    remainder = a % b if b != 0 else "ERROR (modulo by zero)"

    print(f"{'Sum:':13s}{sum}")
    print(f"{'Difference:':13s}{diff}")
    print(f"{'Product:':13s}{product}")
    print(f"{'Quotient:':13s}{quotient}")
    print(f"{'Remainder:':13s}{remainder}")


USAGE = f"""
Usage: python {sys.argv[0]} <number1> <number2>
Example:
    python {sys.argv[0]} 10 3
"""

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("InputError: too many arguments", file=sys.stderr)
        print(USAGE)
        sys.exit(1)
    if len(sys.argv) < 3:
        print("InputError: too few arguments", file=sys.stderr)
        print(USAGE)
        sys.exit(1)

    a: int = None
    b: int = None

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except Exception:
        print("InputError: only numbers", file=sys.stderr)
        print(USAGE)
        sys.exit(1)

    operations(a, b)
