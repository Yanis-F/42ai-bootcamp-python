from NumPyCreator import NumPyCreator as npc
import numpy as np

def test_from_list():
    arr = npc.from_list([1, 2, 3])

    assert np.array_equal(arr, [1, 2, 3])

def test_from_tuple():
    arr = npc.from_tuple((2, 3, 4))

    assert np.array_equal(arr, [2, 3, 4])

def test_from_iterable():
    arr = npc.from_iterable([3, 4, 5])

    assert np.array_equal(arr, [3, 4, 5])

def test_from_shape():
    arr = npc.from_shape((3, 4), 2)

    assert arr.shape == (3, 4)
    assert np.array_equal(arr, [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]])

def test_from_shape():
    arr = npc.from_shape((3, 4), 2)

    assert arr.shape == (3, 4)
    assert np.array_equal(arr, [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]])

def test_from_random():
    arr = npc.random((3, 4))

    assert arr.shape == (3, 4)


def test_from_identity():
    arr = npc.identity(4)

    assert arr.shape == (4, 4)
    assert np.array_equal(arr, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
