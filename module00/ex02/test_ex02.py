from typing import List
from whois import odd_even_or_zero


def run_test(args: List[str], expected: str):
    args.insert(0, "./whois.py")
    assert odd_even_or_zero(args) == expected


def test_empty():
    run_test([], "ERROR")


def test_not_a_number():
    run_test(["Hello"], "ERROR")


def test_several_args():
    run_test(["1", "2"], "ERROR")


def test_several_numbers():
    run_test(["1 2"], "ERROR")


def test_zero():
    run_test(["0"], "I'm Zero.")


def test_one():
    run_test(["1"], "I'm Odd.")


def test_two():
    run_test(["2"], "I'm Even.")


def test_odd():
    run_test(["351"], "I'm Odd.")


def test_even():
    run_test(["894"], "I'm Even.")
