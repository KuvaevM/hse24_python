import numpy as np


def check_conditions(A, B, C, D):
    return (np.sum(A) == np.sum(C)) and (np.any(A != C)) and (not np.any(B != D)) and (np.any(A @ B != C @ D))


while True:
    A = np.random.randint(0, 10, size=(10, 10))
    B = np.random.randint(0, 10, size=(10, 10))
    C = np.random.randint(0, 10, size=(10, 10))
    D = B

    if check_conditions(A, B, C, D):
        break

# Сохраняем матрицы в файлы
np.savetxt('artifacts/3.3/A.txt', A)
np.savetxt('artifacts/3.3/B.txt', B)
np.savetxt('artifacts/3.3/C.txt', C)
np.savetxt('artifacts/3.3/D.txt', D)
