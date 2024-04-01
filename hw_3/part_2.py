import numpy as np


class NumpyMixin:

    def __init__(self, data):
        self._data = np.array(data)

    def save_to_file(self, filename):
        np.savetxt(filename, self.data)

    def __str__(self):
        return str(self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def shape(self):
        return self.data.shape

    @property
    def dtype(self):
        return self.data.dtype

    @property
    def ndim(self):
        return self.data.ndim

    @property
    def size(self):
        return self.data.size


class Matrix(NumpyMixin):
    def __init__(self, data):
        super().__init__(data)

    def __add__(self, other):
        return type(self)(self.data + other.data)

    def __sub__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong matrix size")
        return type(self)(self.data - other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong matrix size")
        return type(self)(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Wrong matrix size")
        return Matrix(np.dot(self.data, other.data))

    def __truediv__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong matrix size")
        return type(self)(self.data / other.data)

    def __pow__(self, power):
        return type(self)(self.data ** power)

    def __eq__(self, other):
        return np.array_equal(self.data, other.data)

    def __getitem__(self, key):
        return type(self)(self.data[key])

    def __setitem__(self, key, value):
        self.data[key] = value


np.random.seed(0)
matrix1_data = np.random.randint(0, 10, (10, 10))
matrix2_data = np.random.randint(0, 10, (10, 10))

matrix1 = Matrix(matrix1_data)
matrix2 = Matrix(matrix2_data)

res_add = matrix1 + matrix2
res_mul_elem = matrix1 * matrix2
res_mul_matrix = matrix1 @ matrix2

res_add.save_to_file("artifacts/3.2/matrix+.txt")
res_mul_elem.save_to_file("artifacts/3.2/matrix*.txt")
res_mul_matrix.save_to_file("artifacts/3.2/matrix@.txt")
