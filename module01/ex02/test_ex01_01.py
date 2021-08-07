from vector import Vector
import pytest


def test_init_empty():
    vec = Vector()

    assert len(vec.values) == 0
    assert vec.size == 0


def test_init_values():
    vec = Vector([42.5, 89.6, 3.14])

    assert vec.values == [42.5, 89.6, 3.14]
    assert vec.size == 3


def test_init_size():
    vec = Vector(4)

    assert vec.values == [0, 1, 2, 3]
    assert vec.size == 4


def test_init_range():
    vec = Vector((42, 50))

    assert vec.values == [42, 43, 44, 45, 46, 47, 48, 49]
    assert vec.size == 8


def test_add_scalar():
    vec = Vector((4, 8))

    vec += 3

    assert vec.values == [7, 8, 9, 10]
    assert vec.size == 4


def test_add_vectors():
    a = Vector((4, 7))
    b = Vector((5, 8))

    vec = a + b

    assert vec.values == [9, 11, 13]
    assert vec.size == 3


def test_add_vectors_length_one():
    a = Vector([5.1])
    b = Vector([42.9])

    vec = a + b

    assert vec.values == [48]
    assert vec.size == 1


def test_add_scalar_length_zero():
    vec = Vector([])

    vec += 3.4

    assert vec.values == []
    assert vec.size == 0


def test_add_vectors_length_zero():
    a = Vector([])
    b = Vector([])

    vec = a + b

    assert vec.values == []
    assert vec.size == 0


def test_add_vectors_diff_lengths():
    a = Vector((4, 7))
    b = Vector((5, 9))

    with pytest.raises(Exception):
        vec = a + b


def test_subt_scalar():
    vec = Vector([4, 6])

    vec -= 3

    assert vec.values == [1, 3]
    assert vec.size == 2


def test_subt_vectors():
    a = Vector([2, 5, 8, 25])
    b = Vector([1, 5, 9, 10])

    vec = a - b

    assert vec.values == [1, 0, -1, 15]
    assert vec.size == 4


def test_subt_vectors_length_one():
    a = Vector([5])
    b = Vector([2])

    vec = a - b

    assert vec.values == [3]
    assert vec.size == 1


def test_subt_scalar_length_zero():
    vec = Vector([])

    vec -= 3.4

    assert vec.values == []
    assert vec.size == 0


def test_subt_vectors_length_zero():
    a = Vector([])
    b = Vector([])

    vec = a - b

    assert vec.values == []
    assert vec.size == 0


def test_subt_vectors_diff_lengths():
    a = Vector([1, 5, 9, 7])
    b = Vector([2, 6, 7])

    with pytest.raises(Exception):
        vec = a - b


def test_mult_scalar():
    vec = Vector([4, 6])

    vec *= 2

    assert vec.values == [8, 12]
    assert vec.size == 2


def test_mult_vectors():
    a = Vector([2, 5, 8, 25])
    b = Vector([1, 5, 9, 10])

    vec = a * b

    assert vec.values == [2, 25, 72, 250]
    assert vec.size == 4


def test_mult_vectors_length_one():
    a = Vector([5])
    b = Vector([2])

    vec = a * b

    assert vec.values == [10]
    assert vec.size == 1


def test_mult_scalar_length_zero():
    vec = Vector([])

    vec *= 3.4

    assert vec.values == []
    assert vec.size == 0


def test_mult_vectors_length_zero():
    a = Vector([])
    b = Vector([])

    vec = a * b

    assert vec.values == []
    assert vec.size == 0


def test_mult_vectors_diff_lengths():
    a = Vector([1, 5, 9, 7])
    b = Vector([2, 6, 7])

    with pytest.raises(Exception):
        vec = a * b


def test_div_scalar():
    vec = Vector([4, 6])

    vec /= 4

    assert vec.values == [1, 1.5]
    assert vec.size == 2


def test_div_scalar_length_zero():
    vec = Vector([])

    vec /= 3.4

    assert vec.values == []
    assert vec.size == 0

def test_dot_length_zero():
    a = Vector([])
    b = Vector([])

    result = a.dot(b)

    assert result == 0

def test_dot_diff_lengths():
    a = Vector([4, 8, 4])
    b = Vector([7, 8, 1, 0])

    with pytest.raises(Exception):
        result = a.dot(b)

def test_dot():
    a = Vector([4, 8, 4, 1])
    b = Vector([7, 8, 1, 0])

    result = a.dot(b)

    assert result == 96
