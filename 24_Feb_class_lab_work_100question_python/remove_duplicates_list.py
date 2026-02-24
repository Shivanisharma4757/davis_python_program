# Program to remove duplicate elements from a list

numbers = [1, 2, 2, 3, 4, 4, 5]       # Create a list with duplicate elements

unique_list = []                      # Create empty list to store unique values

for num in numbers:                   # Loop through each element
    if num not in unique_list:        # Check if element is not already present
        unique_list.append(num)       # Add unique element to new list

print("List without duplicates:", unique_list)   # Display result

# Output Example
# List without duplicates: [1, 2, 3, 4, 5]
