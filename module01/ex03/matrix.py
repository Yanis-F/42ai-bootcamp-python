from typing import Callable, List, Tuple, Union
import operator
import numbers

class Matrix:
    """
    ivar values: List[List[float]] representing the values of the matrix. Access with values[row][column]
    """
    def __init__(self, *args):

        if len(args) == 1:
            arg = args[0]

            if isinstance(arg, list) and all((isinstance(e, list) for e in arg)):
                self.values = arg
            elif type(arg) is tuple:
                self.values = [[0 for _ in range(arg[1])] for __ in range(arg[0])]
            else:
                raise TypeError()
        elif len(args) == 2:
            values = args[0]
            size = args[1]

            if isinstance(values, list) and all((isinstance(e, list) for e in values)) and type(size) is tuple:
                self.values = values
                self.size = size

                if size[0] != len(values) or size[1] != len(values[0]):
                    raise Exception("Given size does not match matrix size")
            else:
                raise TypeError()
        else:
            raise Exception("Expected exactly one or two arguments")

        self.size = (len(self.values), len(self.values[0]))

        if not all([len(row) == self.size[1] for row in self.values]):
            raise Exception("All rows are not equal")
        if self.size[0] == 0 or self.size[1] == 0:
            raise Exception("Matrix size must not be zero")


    def map_matrix(self, op: Callable, other: 'Matrix'):
        if type(other) is Matrix:
            if self.size != other.size:
                raise Exception("Vector sizes should be equal")
            return Matrix([[op(x, y) for x, y in zip(row1, row2)] for row1, row2 in zip(self.values, other.values)])

        raise TypeError()

    def map_scalar(self, op: Callable, scalar):
        if isinstance(scalar, numbers.Number):
            return Matrix([[op(x, scalar) for x in row] for row in self.values])

        raise TypeError()


    def __add__(self, arg: Union['Matrix', float]):
        if type(arg) is Matrix:
            return self.map_matrix(operator.add, arg)
        return self.map_scalar(operator.add, arg)

    def __radd__(self, arg: Union['Matrix', float]):
        return self + arg

    def __sub__(self, arg: Union['Matrix', float]):
        if type(arg) is Matrix:
            return self.map_matrix(operator.sub, arg)
        return self.map_scalar(operator.sub, arg)

    def __rsub__(self, arg: Union['Matrix', float]):
        return self + arg


    def __mul__(self, arg: Union['Matrix', float]):
        if type(arg) is not Matrix:
            return self.map_scalar(operator.mul, arg)
    
        if self.size[1] != arg.size[0]:
            raise Exception("Matrix size incompatible for matrix multiplication")

        result = Matrix((self.size[0], arg.size[1]))

        for r1 in range(self.size[0]):
            for c in range(arg.size[1]):
                for r2 in range(arg.size[0]):
                    result.values[r1][c] += self.values[r1][r2] * arg.values[r2][c]
        
        return result

    def __rmul__(self, arg: Union['Matrix', float]):
        return self + arg

    def __truediv__(self, arg: Union['Matrix', float]):
        return self.map_scalar(operator.truediv, arg)

    def __rtruediv__(self, arg: Union['Matrix', float]):
        return self + arg

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return f"Vector ({self.size}) {str(self.values)}"

    
