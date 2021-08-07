from matrix import Matrix
import pytest


def test_init_no_args():
    with pytest.raises(Exception):
        mat = Matrix()


def test_init_empty():
    with pytest.raises(Exception):
        mat = Matrix([[]])


def test_init_size_row_zero():
    with pytest.raises(Exception):
        mat = Matrix((0, 4))


def test_init_size_column_zero():
    with pytest.raises(Exception):
        mat = Matrix((0, 4))


def test_init_values_one_row():
    mat = Matrix([[42.5, 89.6, 3.14]])

    assert mat.values == [[42.5, 89.6, 3.14]]
    assert mat.size == (1, 3)


def test_init_values_row_size_one():
    mat = Matrix([[42.5], [89.6], [3.14]])

    assert mat.values == [[42.5], [89.6], [3.14]]
    assert mat.size == (3, 1)


def test_init_values():
    mat = Matrix([[42.5, 47.2], [89.6, 134.5], [3.14, 764]])

    assert mat.values == [[42.5, 47.2], [89.6, 134.5], [3.14, 764]]
    assert mat.size == (3, 2)


def test_init_values_inequal_rows():
    with pytest.raises(Exception):
        mat = Matrix([[42.5, 47.2], [89.6, 134.5, 999999], [3.14, 764]])


def test_init_size():
    mat = Matrix((3, 4))

    assert mat.values == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert mat.size == (3, 4)


def test_init_values_and_size():
    mat = Matrix([[0, 7, 4, 4.5], [1, 0, 78, 0], [0.1, 0.5, 60, 47]], (3, 4))

    assert mat.values == [[0, 7, 4, 4.5], [1, 0, 78, 0], [0.1, 0.5, 60, 47]]
    assert mat.size == (3, 4)


def test_init_values_and_incorrect_size():
    with pytest.raises(Exception):
        mat = Matrix([[0, 7, 4, 4.5], [1, 0, 78, 0], [0.1, 0.5, 60, 47]], (3, 5))
    with pytest.raises(Exception):
        mat = Matrix([[0, 7, 4, 4.5], [1, 0, 78, 0], [0.1, 0.5, 60, 47]], (4, 4))


def test_add_scalar():
    mat = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])

    mat += 3

    assert mat.values == [[4, 5, 6, 7], [8, 9, 10, 11]]
    assert mat.size == (2, 4)


def test_add_matrixes():
    a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    b = Matrix([[4, 2, 4, 1], [8, 4, 2, 1]])

    mat = a + b

    assert mat.values == [[5, 4, 7, 5], [13, 10, 9, 9]]
    assert mat.size == (2, 4)


def test_add_matrixes_size_one_one():
    a = Matrix([[5]])
    b = Matrix([[42]])

    mat = a + b

    assert mat.values == [[47]]
    assert mat.size == (1, 1)


def test_add_matrixes_diff_dimention():
    a = Matrix((4, 7))
    b = Matrix((4, 9))
    c = Matrix((5, 9))

    with pytest.raises(Exception):
        mat = a + b
    with pytest.raises(Exception):
        mat = b + c


def test_subt_scalar():
    mat = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])

    mat -= 3

    assert mat.values == [[-2, -1, 0, 1], [2, 3, 4, 5]]
    assert mat.size == (2, 4)


def test_subt_matrixes():
    a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    b = Matrix([[4, 2, 4, 1], [8, 4, 2, 1]])

    mat = a - b

    assert mat.values == [[-3, 0, -1, 3], [-3, 2, 5, 7]]
    assert mat.size == (2, 4)


def test_subt_matrixes_size_one_one():
    a = Matrix([[5]])
    b = Matrix([[42]])

    mat = a - b

    assert mat.values == [[-37]]
    assert mat.size == (1, 1)


def test_subt_matrixes_diff_dimention():
    a = Matrix((4, 7))
    b = Matrix((4, 9))
    c = Matrix((5, 9))

    with pytest.raises(Exception):
        mat = a - b
    with pytest.raises(Exception):
        mat = b - c


def test_mult_scalar():
    mat = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])

    mat *= 3

    assert mat.values == [[3, 6, 9, 12], [15, 18, 21, 24]]
    assert mat.size == (2, 4)


def test_mult_matrixes():
    a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    b = Matrix([[4, 2, 4], [8, 0, 2], [2, 3, 5], [7, 4, 0]])

    mat = a * b

    assert mat.values == [[54, 27, 23], [138, 63, 67]]
    assert mat.size == (2, 3)

def test_mult_matrixes_one_column():
    a = Matrix([[3, 2], [5, 3]])
    b = Matrix([[4], [5]])

    mat = a * b

    assert mat.values == [[22], [35]]
    assert mat.size == (2, 1)

def test_mult_matrixes_result_one_one():
    a = Matrix([[3, 5]])
    b = Matrix([[4], [5]])

    mat = a * b

    assert mat.values == [[37]]
    assert mat.size == (1, 1)

def test_mult_matrixes_one_row():
    a = Matrix([[3, 5, 11]])
    b = Matrix([[4, 3, 2], [3, 3, 3], [2, 3, 4]])

    mat = a * b

    assert mat.values == [[49, 57, 65]]
    assert mat.size == (1, 3)
def test_mult_matrixes_size_one_one():
    a = Matrix([[5]])
    b = Matrix([[42]])

    mat = a * b

    assert mat.values == [[210]]
    assert mat.size == (1, 1)


def test_mult_matrixes_incompatible_dimention():
    a = Matrix((4, 7))
    b = Matrix((4, 9))

    with pytest.raises(Exception):
        mat = a * b


def test_div_scalar():
    mat = Matrix([[4, 6], [12, 24]])

    mat /= 4

    assert mat.values == [[1, 1.5], [3, 6]]
    assert mat.size == (2, 2)

