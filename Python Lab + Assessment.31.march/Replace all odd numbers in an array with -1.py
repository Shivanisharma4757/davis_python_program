import numpy as np

# Input: NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Replace odd numbers with -1
arr[arr % 2 != 0] = -1

# Output
print("Modified array:", arr)

#output
#Modified array: [-1  2 -1  4 -1  6 -1]
