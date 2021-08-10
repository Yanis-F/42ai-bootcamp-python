import numpy as np

class NumPyCreator:

    def from_list(lst):
        return np.array(lst)

    def from_tuple(tpl):
        return np.array(tpl)
    
    def from_iterable(iterable):
        return np.array(iterable)

    def from_shape(shape, value):
        return np.ones(shape) * value

    def random(shape):
        return np.random.default_rng().random(shape)

    def identity(n):
        return np.eye(n)