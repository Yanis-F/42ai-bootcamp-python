from operations import operations


def run_test(capsys, a: int, b: int, expected_out: str, expected_err: str = ""):
    operations(a, b)
    captured = capsys.readouterr()
    assert captured.out == expected_out
    assert captured.err == expected_err


def test_basic(capsys):
    run_test(capsys, 42, 10,
             """Sum:         52
Difference:  32
Product:     420
Quotient:    4.2
Remainder:   2
""")


def test_zero(capsys):
    run_test(capsys, 45, 0,
             """Sum:         45
Difference:  45
Product:     0
Quotient:    ERROR (div by zero)
Remainder:   ERROR (modulo by zero)
""")


def test_non_numbers(capsys):
    run_test(capsys, "one", "two", "", "InputError: only numbers\n")
