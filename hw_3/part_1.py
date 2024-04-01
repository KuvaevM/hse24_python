import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong matrix size")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong matrix size")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Wrong matrix size")
        return Matrix(np.dot(self.data, other.data))

    def save_to_file(self, filename):
        np.savetxt(filename, self.data)


np.random.seed(0)
matrix1_data = np.random.randint(0, 10, (10, 10))
matrix2_data = np.random.randint(0, 10, (10, 10))

matrix1 = Matrix(matrix1_data)
matrix2 = Matrix(matrix2_data)

res_add = matrix1 + matrix2
res_mul_elem = matrix1 * matrix2
res_mul_matrix = matrix1 @ matrix2

res_add.save_to_file("artifacts/3.1/matrix+.txt")
res_mul_elem.save_to_file("artifacts/3.1/matrix*.txt")
res_mul_matrix.save_to_file("artifacts/3.1/matrix@.txt")
