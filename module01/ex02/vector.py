from typing import Callable, List, Tuple, Union
import operator
import numbers

class Vector:
    def __init__(self, arg: Union[List[float], int, Tuple[int, int]] = None):
        if arg is None:
            self.values = []
        elif type(arg) is list:
            self.values = arg
        elif type(arg) is int:
            self.values = list(range(arg))
        elif type(arg) is tuple:
            self.values = list(range(arg[0], arg[1]))
        else:
            raise TypeError()

        self.size = len(self.values)


    def map_vector(self, op: Callable, other: 'Vector'):
        if type(other) is Vector:
            if self.size != other.size:
                raise Exception("Vector sizes should be equal")
            return Vector([op(x, y) for x, y in zip(self.values, other.values)])

        raise TypeError()

    def map_scalar(self, op: Callable, scalar):
        if isinstance(scalar, numbers.Number):
            return Vector([op(x, scalar) for x in self.values])

        raise TypeError()


    def __add__(self, arg: Union['Vector', float]):
        if type(arg) is Vector:
            return self.map_vector(operator.add, arg)
        return self.map_scalar(operator.add, arg)

    def __radd__(self, arg: Union['Vector', float]):
        return self + arg

    def __sub__(self, arg: Union['Vector', float]):
        if type(arg) is Vector:
            return self.map_vector(operator.sub, arg)
        return self.map_scalar(operator.sub, arg)

    def __rsub__(self, arg: Union['Vector', float]):
        return self + arg


    def __mul__(self, arg: Union['Vector', float]):
        if type(arg) is Vector:
            return self.map_vector(operator.mul, arg)
        return self.map_scalar(operator.mul, arg)

    def __rmul__(self, arg: Union['Vector', float]):
        return self + arg

    def __truediv__(self, arg: Union['Vector', float]):
        return self.map_scalar(operator.truediv, arg)

    def __rtruediv__(self, arg: Union['Vector', float]):
        return self + arg


    def dot(self, arg: 'Vector'):
        if type(arg) is Vector:
            return sum([v for v in (self * arg).values])
        raise TypeError()

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return f"Vector ({self.size}) {str(self.values)}"

    
