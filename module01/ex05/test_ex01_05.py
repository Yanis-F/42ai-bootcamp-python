from eval import Evaluator
from typing import List

def run_test(coefs: List[float], words: List[str], expected: float):
    assert Evaluator.zip_evaluate(coefs, words) == expected
    assert Evaluator.enumerate_evaluate(coefs, words) == expected

def test_empty():
    run_test([], [], 0)

def test_uneven_lists():
    run_test([1], ["hello", "world"], -1)
    run_test([0.0, -1.0, 1.0, -12.0, 0.0, 42.42], ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"], -1)

def test_plausible_use():
    run_test([1.0, 2.0, 1.0, 4.0, 0.5], ["Le", "Lorem", "Ipsum", "est", "simple"], 32)