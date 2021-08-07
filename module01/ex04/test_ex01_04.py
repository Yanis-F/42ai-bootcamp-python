import pytest
from generator import generator

def test_invalid_option():
    with pytest.raises(Exception):
        list(generator("Hello world", " ", "kebab"))


def test_empty():
    aslist = list(generator("", " "))

    assert aslist == []

def test_basic():
    idx = 0
    lst = ["Le", "Lorem", "Ipsum", "est", "simplement", "du", "faux", "texte."]

    for word in generator("Le Lorem Ipsum est simplement du faux texte.", sep=" "):
        assert idx < len(lst)
        assert word == lst[idx]
        idx += 1
    assert idx == len(lst)

def test_shuffle():
    expected = ["Le", "Lorem", "Ipsum", "est", "simplement", "du", "faux", "texte."]
    actual = list(generator("Le Lorem Ipsum est simplement du faux texte.", sep=" ", option="shuffle"))

    assert len(expected) == len(actual)

    for w in actual:
        assert w in expected

def test_unique():
    expected = ["Le", "Lorem", "Ipsum", "est", "simplement", "du", "faux", "texte."]
    actual = list(generator("Le Lorem Ipsum Lorem est simplement est du faux texte. est", sep=" ", option="unique"))

    assert expected == actual
