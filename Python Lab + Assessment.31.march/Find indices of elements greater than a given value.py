import numpy as np

# Input: NumPy array and value
arr = np.array([10, 25, 30, 15, 5, 40])
value = 20

# Find indices where elements are greater than given value
indices = np.where(arr > value)

# Output
print("Array:", arr)
print("Indices of elements greater than", value, ":", indices[0])

#output
#Array: [10 25 30 15  5 40]
#Indices of elements greater than 20 : [1 2 5]
