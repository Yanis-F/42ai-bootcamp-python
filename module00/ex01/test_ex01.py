from typing import List
from exec import reverse_and_swap_case

def run_test(args: List[str], expected: str):
    assert reverse_and_swap_case(args) == expected

def test_empty():
    run_test([], "")

def test_one_word():
    run_test(["Hello"], "OLLEh")

def test_several_args():
    run_test(["Hello", "python", "world"], "DLROW NOHTYP OLLEh")

def test_special_signs():
    run_test(["I like 123=-\\';][|<>\""], "\"><|[];'\\-=321 EKIL i")

def test_several_spaces_in_one_arg():
    run_test(["Hello", "python     world"], "DLROW     NOHTYP OLLEh")
