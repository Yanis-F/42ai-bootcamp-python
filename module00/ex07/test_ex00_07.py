import pytest
from filterwords import filter_words


def test_empty():
    assert filter_words(["./filterwords.py", "", 3]) == []


def test_length_zero():
    with pytest.raises(Exception) as e:
        filter_words(["./filterwords.py", "Hello world", "0"])



def test_length_one():
    assert filter_words(
        ["./filterwords.py", "Hello world", "1"]) == ["Hello", "world"]


def test_length_negative():
    with pytest.raises(Exception) as e:
        filter_words(["./filterwords.py", "Hello world", "-1"])


def test_too_few_args():
    with pytest.raises(Exception) as e:
        filter_words(["./filterwords.py", "Hello world"])



def test_too_much_args():
    with pytest.raises(Exception) as e:
        filter_words(["./filterwords.py", "Hello", "world", "3"])



def test_plausible_example():
    assert filter_words(["./filterwords.py", "A robot must protect its own existence as long as such protection does not conflict with the First or Second Law", "6"]) \
        == ['protect', 'existence', 'protection', 'conflict']

def test_punctuation():
    assert filter_words(["./filterwords.py", "This..text's_words89 are!!!,fairly hard-to separate, isn't it??", "4"]) \
        == ['s_words89', 'fairly', 'hard-to', 'separate']
