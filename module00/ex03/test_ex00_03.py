import io
from count import text_analyzer


def run_test(capsys, text: str, expected: str):
    text_analyzer(text)
    captured = capsys.readouterr()
    assert captured.out == expected
    assert captured.err == ""


def test_empty(capsys):
    run_test(capsys, "", 
    """The text contains 0 characters:
- 0 upper letters
- 0 lower letters
- 0 punctuation marks
- 0 spaces
""")

def test_one_lowercase_char(capsys):
    run_test(capsys, "a", """The text contains 1 character:
- 0 upper letters
- 1 lower letter
- 0 punctuation marks
- 0 spaces
""")

def test_one_uppercase_char(capsys):
    run_test(capsys, "J", """The text contains 1 character:
- 1 upper letter
- 0 lower letters
- 0 punctuation marks
- 0 spaces
""")


def test_one_puncuation_mark(capsys):
    run_test(capsys, ".", """The text contains 1 character:
- 0 upper letters
- 0 lower letters
- 1 punctuation mark
- 0 spaces
""")

def test_one_space(capsys):
    run_test(capsys, " ", """The text contains 1 character:
- 0 upper letters
- 0 lower letters
- 0 punctuation marks
- 1 space
""")

def test_complete_1(capsys):
    run_test(capsys, "Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.",
"""The text contains 143 characters:
- 2 upper letters
- 113 lower letters
- 4 punctuation marks
- 18 spaces
""")

def test_complete_2(capsys):
    run_test(capsys, "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.",
"""The text contains 234 characters:
- 5 upper letters
- 187 lower letters
- 8 punctuation marks
- 30 spaces
""")

def test_no_arg(capsys, monkeypatch):

    monkeypatch.setattr('sys.stdin', io.StringIO('Hello world\n'))
    text_analyzer()
    captured = capsys.readouterr()
    assert captured.out == """What is the text to analyse?
The text contains 11 characters:
- 1 upper letter
- 9 lower letters
- 0 punctuation marks
- 1 space
"""
    assert captured.err == ""

def test_two_args(capsys):
    text_analyzer("Hello", "world")
    captured = capsys.readouterr()
    assert captured.err == "ERROR\n"
    assert captured.out == ""
