from sympy import Matrix

# Define the matrix from the image provided
matrix_to_find_rank = Matrix([
    [1, 2, 4, 3, 4],
    [2, 4, 3, 1, 3],
    [1, 3, 2, 2, 1],
    [1, 4, 0, 1, 3],
    [2, 2, 3, 3, 4]
])

# Find the rank of the matrix
rank = matrix_to_find_rank.rank()
print(rank)
