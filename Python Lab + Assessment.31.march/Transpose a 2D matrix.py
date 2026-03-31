import numpy as np

# Input: 2D NumPy array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Transpose of the matrix
transpose_matrix = matrix.T

# Output
print("Original Matrix:\n", matrix)
print("Transposed Matrix:\n", transpose_matrix)

#output
#Original Matrix:
 #[[1 2 3]
 #[4 5 6]]
#Transposed Matrix:
# [[1 4]
# [2 5]
# [3 6]]
