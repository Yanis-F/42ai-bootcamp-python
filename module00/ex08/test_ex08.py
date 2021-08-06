from sos import text2morse
import pytest

def test_empty():
    assert text2morse("") == ""

def test_only_space():
    assert text2morse("    ") == ""

def test_non_alpha():
    with pytest.raises(Exception) as e:
        text2morse("my friend's house is open")



def test_one_letter():
    assert text2morse("i") == ".."


def test_capitals():
    assert text2morse("SOs") == "... --- ..."


def test_spaces():
    assert text2morse("sos SOS") == "... --- ... / ... --- ..."


def test_plausible_example():
    assert text2morse(
        "96 BOULEVARD Bessiere") == "----. -.... / -... --- ..- .-.. . ...- .- .-. -.. / -... . ... ... .. . .-. ."
