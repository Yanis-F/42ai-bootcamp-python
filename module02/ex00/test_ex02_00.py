from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce


def test_map_empty():
    assert list(ft_map(lambda x: x + 1, [])) == []


def test_map_basic():
    assert list(ft_map(lambda x: x + 1, [2, 3, 4])) == [3, 4, 5]


def test_filter_empty():
    assert list(ft_filter(lambda x: x % 2 == 1, [])) == []


def test_filter_basic():
    assert list(ft_filter(lambda x: x % 2 == 1, [2, 3, 4, 5, 7])) == [3, 5, 7]


def test_reduce_empty():
    assert ft_reduce(lambda x, y: x * y, []) == None


def test_reduce_basic():
    assert ft_reduce(lambda x, y: x * y, [2, 3, 4, 5, 7]) == (2*3*4*5*7)
