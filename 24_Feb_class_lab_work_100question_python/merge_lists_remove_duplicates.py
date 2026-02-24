# Program to merge two lists and remove duplicates

list1 = [1, 2, 3, 4]                   # Create first list
list2 = [3, 4, 5, 6]                   # Create second list

merged = list1 + list2                 # Merge both lists

unique = []                            # Create empty list for unique elements

for num in merged:                     # Loop through merged list
    if num not in unique:              # Check if element is not already present
        unique.append(num)             # Add unique element

print("Merged list without duplicates:", unique)  # Display result

# Output Example
# Merged list without duplicates: [1, 2, 3, 4, 5, 6]
