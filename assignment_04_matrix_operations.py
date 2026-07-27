# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(label):
    """Read an M x N matrix from the user."""
    rows = int(input(f"[{label}] Enter number of rows: "))
    cols = int(input(f"[{label}] Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"[{label}] Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix, rows, cols


def display_matrix(matrix):
    """Display a matrix in a neat, aligned grid format."""
    for row in matrix:
        print("\t".join(str(val) for val in row))


def transpose_matrix(matrix, rows, cols):
    """Compute the transpose of a matrix."""
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

def add_matrices(a, b, rows, cols):
    """Compute the element-wise sum of two matrices."""
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


def multiply_matrices(a, b, m, n, p):
    """Compute the matrix product A x B."""
    result = []
    for i in range(m):
        row = []
        for j in range(p):
            cell_sum = 0
            for k in range(n):
                cell_sum += a[i][k] * b[k][j]
            row.append(cell_sum)
        result.append(row)
    return result


print("========== PART A — Transpose a Matrix ==========")
matrix, rows, cols = read_matrix("Part A")
print("\nOriginal Matrix:")
display_matrix(matrix)
transposed = transpose_matrix(matrix, rows, cols)
print("\nTransposed Matrix:")
display_matrix(transposed)

print("\n========== PART B — Add Two Matrices ==========")
a1, r1, c1 = read_matrix("Matrix A")
a2, r2, c2 = read_matrix("Matrix B")

if r1 != r2 or c1 != c2:
    print("Error: Matrices must have the same dimensions for addition.")
else:
    print("\nMatrix A:")
    display_matrix(a1)
    print("Matrix B:")
    display_matrix(a2)
    result_add = add_matrices(a1, a2, r1, c1)
    print("Sum (A + B):")
    display_matrix(result_add)

print("\n========== PART C — Multiply Two Matrices ==========")
ma, m_rows, m_cols = read_matrix("Matrix A")
mb, _, mb_cols = read_matrix("Matrix B")

if m_cols != (len(mb)):
    print("Error: Columns of A must equal rows of B for multiplication.")
else:
    print("\nMatrix A:")
    display_matrix(ma)
    print("Matrix B:")
    display_matrix(mb)
    result_mul = multiply_matrices(ma, mb, m_rows, m_cols, mb_cols)
    print("Product (A x B):")
    display_matrix(result_mul)