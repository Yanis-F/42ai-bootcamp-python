import numpy as np


class ScrapBooker:

    def crop(array, dimensions, position = (0, 0)):
        newsize = tuple(x - y for x, y in zip(array.shape, position))
        
        if any(x <= 0 for x in newsize):
            raise Exception("Position out of bounds")

        if any(x > y for x, y in zip(dimensions, newsize)):
            raise Exception("Dimension out of bounds for position")

        return np.array(array
            [
                position[0]:position[0]+dimensions[0], 
                position[1]:position[1]+dimensions[1]
            ])

    def thin(array, n, axis):
        mask = np.ones(array.size, dtype=bool)
        mask[n-1::n] = 0

        if axis == 0:
            return np.array(array[mask[:array.shape[0]]])
        if axis == 1:   
            return np.array(array[:,mask[:array.shape[1]]])
        raise Exception("invalid axis (0 or 1)")

    def juxtapose(array, n, axis):
        if axis == 0:
            return np.array([row for row in array] * n)
        if axis == 1:
            return np.array([[elem for elem in row] * n for row in array])
        raise Exception("invalid axis (0 or 1)")

    def mosaic(array, dimensions):
        return ScrapBooker.juxtapose(ScrapBooker.juxtapose(array, dimensions[0], 0), dimensions[1], 1)