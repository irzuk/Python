import numpy as np


class ToStrMixin:
    def __str__(self):
        s = ''
        for line in self.data:
            s += str(line) + '\n'
        return s

class SaveMixin:
    def saveToFile(self, file):
        with open(file, 'w') as f:
            f.write(str(self))

class GetSetMixin:
    def set_data(self, new_data):
        self.data = new_data


    def get_first_dimention(self):
        return self.size[0]

    def get_second_dimention(self):
        return self.size[1]

    def get_data(self):
        return self.data


class Matrix:
    def __init__(self, l):
        self.data = l
        self.size = [len(self.data), len(self.data[0])]


class FinalMatrix(Matrix,np.lib.mixins.NDArrayOperatorsMixin, SaveMixin, GetSetMixin, ToStrMixin):
    _HANDLED_TYPES = (Matrix,)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (Matrix,)):
                return NotImplemented

        inputs = tuple(x.data if isinstance(x, Matrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.data if isinstance(x, Matrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)


left = FinalMatrix(np.random.randint(0, 10, (10, 10)))
right = FinalMatrix(np.random.randint(0, 10, (10, 10)))

(left @ right).saveToFile('./artifacts/medium/matrix@.txt')
(left + right).saveToFile('./artifacts/medium/matrix+.txt')
(left * right).saveToFile('./artifacts/medium/matrix*.txt')
