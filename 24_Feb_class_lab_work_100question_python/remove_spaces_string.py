# Program to remove all spaces from a string

text = input("Enter a string: ")            # Take string input from user

result = text.replace(" ", "")              # Replace all spaces with empty character

print("String without spaces:", result)     # Display modified string

# Output Example
# Enter a string: python is easy
# String without spaces: pythoniseasy
