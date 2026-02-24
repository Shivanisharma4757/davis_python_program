# Program to find the largest element in a list

numbers = [10, 45, 23, 89, 12]        # Create a list of numbers

largest = numbers[0]                  # Assume first element is the largest

for num in numbers:                   # Loop through each element in the list
    if num > largest:                 # Check if current element is greater than largest
        largest = num                 # Update largest value

print("Largest element:", largest)    # Display the largest element

# Output Example
# Largest element: 89
