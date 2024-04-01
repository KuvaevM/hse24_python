import numpy as np

class NumpyMixin:
    def __init__(self, data):
        self._data = np.array(data)

    def __str__(self):
        return str(self.data)

    @property
    def data(self):
        return self._data

    def __hash__(self):
        return int(np.sum(self.data)) # sum of all matrix elements

    def save_to_file(self, filename):
        np.savetxt(filename, self.data)

    def from_file(self, filename):
        data = np.loadtxt(filename)
        return type(self)(data)


class Matrix(NumpyMixin):
    def __init__(self, data):
        super().__init__(data)

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong matrix size")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong matrix size")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        print("aaa")
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Wrong matrix size")
        result = Matrix(np.dot(self.data, other.data))
        self._cached_result = super.__hash__(result)
        print(self._cached_result)
        return Matrix(np.dot(self.data, other.data))


A = Matrix(np.loadtxt('artifacts/3.3/A.txt'))
B = Matrix(np.loadtxt('artifacts/3.3/B.txt'))
C = Matrix(np.loadtxt('artifacts/3.3/C.txt'))
D = Matrix(np.loadtxt('artifacts/3.3/D.txt'))

AB = A @ B
CD = C @ D

np.savetxt('artifacts/3.3/AB.txt', AB.data)
np.savetxt('artifacts/3.3/CD.txt', CD.data)

with open('artifacts/3.3/hash.txt', 'w') as f:
    f.write(f'Hash of AB: {hash(AB)}\n')
    f.write(f'Hash of CD: {hash(CD)}')
