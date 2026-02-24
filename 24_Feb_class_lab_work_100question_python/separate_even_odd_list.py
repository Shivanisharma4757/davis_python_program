# Program to separate even and odd numbers from a list

numbers = [1, 2, 3, 4, 5, 6]           # Create a list of numbers

even = []                              # Create empty list for even numbers
odd = []                               # Create empty list for odd numbers

for num in numbers:                    # Loop through each element
    if num % 2 == 0:                   # Check if number is even
        even.append(num)               # Add to even list
    else:                              # Otherwise
        odd.append(num)                # Add to odd list

print("Even numbers:", even)           # Display even numbers
print("Odd numbers:", odd)             # Display odd numbers

# Output Example
# Even numbers: [2, 4, 6]
# Odd numbers: [1, 3, 5]
