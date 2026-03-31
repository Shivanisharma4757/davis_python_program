import numpy as np

# Input: Two matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Matrix multiplication
result = np.dot(A, B)

# Output
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Result matrix:\n", result)

#output
#Matrix A:
 #[[1 2]
 # [3 4]]

#Matrix B:
# [[5 6]
#  [7 8]]

#Result matrix:
# [[19 22]
#  [43 50]]
