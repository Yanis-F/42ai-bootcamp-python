from ScrapBooker import ScrapBooker
import numpy as np


def test_crop():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

    newarr = ScrapBooker.crop(arr, (2, 2), (0, 1))

    np.testing.assert_array_equal(newarr, 
        np.array([[2, 3], [6, 7]])
    )

def test_thin():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    thinVer = ScrapBooker.thin(arr, 3, 0)
    thinHor = ScrapBooker.thin(arr, 3, 1)

    np.testing.assert_array_equal(thinVer, 
        np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    )
    np.testing.assert_array_equal(thinHor,  
        np.array([[1, 2, 4], [5, 6, 8], [9, 10, 12]])
    )

def test_juxtapose():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    juxVer = ScrapBooker.juxtapose(arr, 3, 0)
    juxHor = ScrapBooker.juxtapose(arr, 3, 1)

    np.testing.assert_array_equal(juxVer, 
        np.array([
            [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
            [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
            [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
        ])
    )
    np.testing.assert_array_equal(juxHor,  
        np.array([[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4], [5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8], [9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12]])
    )

def test_mosaic():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    newArr = ScrapBooker.mosaic(arr, (3, 2))

    np.testing.assert_array_equal(newArr, 
        np.array([
            [1, 2, 3, 4, 1, 2, 3, 4], [5, 6, 7, 8, 5, 6, 7, 8], [9, 10, 11, 12, 9, 10, 11, 12],
            [1, 2, 3, 4, 1, 2, 3, 4], [5, 6, 7, 8, 5, 6, 7, 8], [9, 10, 11, 12, 9, 10, 11, 12],
            [1, 2, 3, 4, 1, 2, 3, 4], [5, 6, 7, 8, 5, 6, 7, 8], [9, 10, 11, 12, 9, 10, 11, 12],
        ]))