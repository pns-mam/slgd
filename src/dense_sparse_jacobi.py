import numpy as np
import scipy.sparse as sparse
from scipy.sparse import csr_matrix
import time


def generate_corrected_sparse_tridiagonal_matrix(n, diagonal_value=5, off_diagonal_value=1):
    """
    Generates a sparse tridiagonal matrix, ensuring no overlaps.

    Args:
        n: Dimension of the system (size of the matrix A).
        diagonal_value: Value for the diagonal elements.
        off_diagonal_value: Value for the off-diagonal elements.

    Returns:
        A: Sparse coefficient matrix (scipy.sparse.csr_matrix).
        b: Right-hand side vector (numpy array).
    """
    ### TODO: Complete code here 
    # Main diagonal
    main_diag = np.full(n, diagonal_value+off_diagonal_value)

    # Construct sparse matrix
    data = main_diag
    #print(data)
    rows = np.arange(n) # might need to use np.concatenate
    #print(rows)
    cols = np.arange(n)
    #print(cols)
    As = csr_matrix((data, (rows, cols)), shape=(n, n))

    # Construct dense matrix for reference
    A_dense = np.zeros((n, n))
    for i in range(n):
        A_dense[i, i] = diagonal_value+off_diagonal_value

    b = np.zeros_like(x0)
    return As, A_dense, b



def jacobi_dense(A, b, x0, tol=1e-6, max_iter=1000):
    """
    Jacobi method for dense matrices.

    Args:
        A: Dense coefficient matrix (numpy array).
        b: Right-hand side vector (numpy array).
        x0: Initial guess for the solution vector (numpy array).
        tol: Tolerance for convergence.
        max_iter: Maximum number of iterations.

    Returns:
        x: Approximate solution vector.
        iterations: Number of iterations performed.
        time_taken: Time taken for the iterations.
    """
    ### TODO: Code your thing here!
    start_time = time.time()
    x_new = x0.copy()
    end_time = time.time()
    time_taken = end_time - start_time
    return x_new, 1, time_taken

def jacobi_sparse(A, b, x0, tol=1e-7, max_iter=10000):
    """
    Jacobi method for sparse matrices.

    Args:
        A: Sparse coefficient matrix (scipy.sparse.csr_matrix).
        b: Right-hand side vector (numpy array).
        x0: Initial guess for the solution vector (numpy array).
        tol: Tolerance for convergence.
        max_iter: Maximum number of iterations.

    Returns:
        x: Approximate solution vector.
        iterations: Number of iterations performed.
        time_taken: Time taken for the iterations.
    """
    ### TODO: Adapt code here
    x_new = x0.copy()
    start_time = time.time()
    end_time = time.time()
    time_taken = end_time - start_time
    return x_new, 1, time_taken

# Example usage:
n=10000 
x0 = np.zeros(n)  ## initial guess
A_sparse, A_dense_v1, b = generate_corrected_sparse_tridiagonal_matrix(n) 
A_dense_v2 = A_sparse.toarray()  # Convert to dense format for comparison





# Classical Jacobi (dense)
x_dense, iter_dense, time_dense = jacobi_dense(A_dense_v2, b, x0) 

# Jacobi for sparse matrix
x_sparse, iter_sparse, time_sparse = jacobi_sparse(A_sparse, b, x0)

print(f"Iterations (dense): {iter_dense}, Time (dense): {time_dense:.4f} seconds")
print(f"Iterations (sparse): {iter_sparse}, Time (sparse): {time_sparse:.4f} seconds")

#x_exact = np.linalg.solve(A_dense_v2, b)
#print(x_exact)
#print(x_sparse)

### TODO: 
# Implement a small for loop comparing the times required for both approaches as a function of the dimension n
