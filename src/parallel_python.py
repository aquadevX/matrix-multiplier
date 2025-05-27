from multiprocessing import Pool, cpu_count

def _compute_row(args):
    A_row, B = args
    return [sum(a * b for a, b in zip(A_row, col)) for col in zip(*B)]

def multiply_matrices_parallel(A, B):
    with Pool(cpu_count()) as pool:
        result = pool.map(_compute_row, [(row, B) for row in A])
    return result
