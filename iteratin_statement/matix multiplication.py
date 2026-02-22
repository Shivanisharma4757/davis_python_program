# Program to multiply two matrices in Python

# Define first matrix (2x3)
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Define second matrix (3x2)
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Get dimensions
rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

# Check if multiplication is possible
if cols_A != rows_B:
    print("Matrix multiplication not possible")
else:
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Multiply matrices using nested loops
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or k in range(rows_B)
                result[i][j] += A[i][k] * B[k][j]
    
    # Print the result matrix
    print("Resultant Matrix:")
    for row in result:
        print(row)
