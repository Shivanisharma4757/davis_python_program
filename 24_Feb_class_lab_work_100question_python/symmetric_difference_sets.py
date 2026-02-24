# Program to find symmetric difference of two sets

set1 = {1, 2, 3, 4}                 # Create first set
set2 = {3, 4, 5, 6}                 # Create second set

result = set1.symmetric_difference(set2)  # Find elements not common in both sets

print("Symmetric difference:", result)    # Display result

# Output Example
# Symmetric difference: {1, 2, 5, 6}
