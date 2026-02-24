# Program to check whether tuple elements are unique

numbers = (1, 2, 3, 4, 5)             # Create a tuple

unique = True                         # Assume elements are unique

for i in range(len(numbers)):         # Outer loop through tuple
    for j in range(i + 1, len(numbers)):  # Inner loop to compare elements
        if numbers[i] == numbers[j]:  # Check if duplicate found
            unique = False            # Mark as not unique

if unique:                            # Check result
    print("All elements are unique")  # Display unique result
else:                                 # Otherwise
    print("Duplicate elements found") # Display duplicate result

# Output Example
# All elements are unique
