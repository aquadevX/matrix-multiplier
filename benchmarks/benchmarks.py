import time
import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.pure_python import multiply_matrices
from src.numpy_version import multiply_matrices_numpy
from src.parallel_python import multiply_matrices_parallel

def generate_matrix(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

def benchmark():
    sizes = [10, 100, 200, 300]
    print("Matrix Size | Python Time (s) | NumPy Time (s) | Parallel Time (s)")
    print("---------------------------------------------------------------")
    for size in sizes:
        A = generate_matrix(size)
        B = generate_matrix(size)

        start = time.time()
        multiply_matrices(A, B)
        python_time = time.time() - start

        start = time.time()
        multiply_matrices_numpy(A, B)
        numpy_time = time.time() - start

        start = time.time()
        multiply_matrices_parallel(A, B)
        parallel_time = time.time() - start

        print(f"{size:10d} | {python_time:.5f}       | {numpy_time:.5f}     | {parallel_time:.5f}")

if __name__ == "__main__":
    benchmark()
