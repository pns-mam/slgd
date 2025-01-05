import numpy as np
import time

def compute_inverse(n):
    """
    Computes the inverse of a random square matrix of size n.

    Args:
      n: Size of the matrix.

    Returns:
      The inverse of the matrix.
    """
    A = np.random.rand(n, n)
    start_time = time.time()
    A_inv = np.linalg.inv(A)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return A_inv, elapsed_time

# Example usage
matrix_sizes = [10, 100, 500, 1000, 10000, 20000]  # Adjust sizes as needed
for n in matrix_sizes:
    A_inv, elapsed_time = compute_inverse(n)
    print(f"Matrix size: {n} x {n}")
    print(f"Elapsed time: {elapsed_time:.4f} seconds")
    print("-" * 20)