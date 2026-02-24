# Program to check whether a list is palindrome

numbers = [1, 2, 3, 2, 1]                # Create a list

if numbers == numbers[::-1]:             # Compare list with its reverse
    print("Palindrome List")             # Display palindrome result
else:                                    # Otherwise
    print("Not a Palindrome List")       # Display not palindrome

# Output Example
# Palindrome List
