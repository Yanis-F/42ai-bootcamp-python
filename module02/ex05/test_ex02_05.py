from TinyStatistician import *


def test_mean_empty():
    assert TinyStatistician.mean([]) == None


def test_mean_one_value():
    assert TinyStatistician.mean([42]) == 42


def test_mean_plausible_input():
    assert TinyStatistician.mean([1, 42, 300, 10, 59]) == 82.4


def test_median_empty():
    assert TinyStatistician.median([]) == None


def test_median_one_value():
    assert TinyStatistician.median([42]) == 42


def test_median_plausible_input():
    assert TinyStatistician.median([1, 42, 300, 10, 59]) == 42


def test_quartile_empty():
    assert TinyStatistician.quartile([], 20) == None


def test_quartile_one_value():
    assert TinyStatistician.quartile([42], 25) == 42


def test_quartile_plausible_input():
    assert TinyStatistician.quartile([1, 42, 300, 10, 59], 25) == 10
    assert TinyStatistician.quartile([1, 42, 300, 10, 59], 50) == 42
    assert TinyStatistician.quartile([1, 42, 300, 10, 59], 75) == 59


def test_var_empty():
    assert TinyStatistician.var([]) == None


def test_var_one_value():
    assert TinyStatistician.var([42]) == 0


def test_var_plausible_input():
    assert math.isclose(TinyStatistician.var([1, 42, 300, 10, 59]), 12279.44)


def test_std_empty():
    assert TinyStatistician.std([]) == None


def test_std_one_value():
    assert TinyStatistician.std([42]) == 0


def test_std_plausible_input():
    assert math.isclose(TinyStatistician.std([1, 42, 300, 10, 59]), 110.81263465868862)
