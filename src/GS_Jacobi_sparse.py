import numpy as np
import scipy.sparse as sparse
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt

def generate_simple_sparse_tridiagonal_matrix(n, diagonal_value=10, off_diagonal_value=4):
    """
    Generates a sparse tridiagonal matrix, ensuring no overlaps.

    Args:
        n: Dimension of the system (size of the matrix A).
        diagonal_value: Value for the diagonal elements.
        off_diagonal_value: Value for the off-diagonal elements.

    Returns:
        A: Sparse coefficient matrix (scipy.sparse.csr_matrix).
        A_dense: equivalent Dense matrix (numpy array)
        b: Right-hand side vector (numpy array).
    """
    ### TODO: Fill your code here
    As = csr_matrix((n, n)) # Generates CSR Matrix from COO representation

    # Construct dense matrix for reference
    A_dense = np.zeros((n, n))
    for i in range(n):
        A_dense[i, i] = diagonal_value

    b = np.zeros(n)
    return As, A_dense, b

def generate_sparse_tridiagonal_matrix(n):
    """
    Generates a sparse tridiagonal matrix with the specific values.

    Args:
        n: Dimension of the system (size of the matrix A).

    Returns:
        A: Sparse coefficient matrix (scipy.sparse.csr_matrix).
        b: Right-hand side vector (numpy array).
    """
    ### TODO: Fill your code here.
    A = csr_matrix((n, n))

    # Construct dense matrix for reference
    A_dense = np.zeros((n, n))
    
    # Right-hand side vector
    b = np.zeros(n)

    return A,  A_dense, b



def jacobi_sparse_with_error(A, b, x0, x_exact, tol=eps, max_iter=iteration):
    ### TODO: 
    # Add comments first. 
    # Add your code
    return x0, 0, []


def gauss_seidel_sparse_with_error(A, b, x0, x_exact, tol=eps, max_iter=iteration):
    ### TODO: 
    # Add comments first. 
    # Add your code
    return x0, 0, []

### TODO: 
# Set up all the important parameters
# Set up all useful plotting tools
