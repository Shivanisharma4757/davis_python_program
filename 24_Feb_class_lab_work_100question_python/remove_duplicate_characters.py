# Program to remove duplicate characters from a string

text = input("Enter a string: ")            # Take string input

result = ""                                 # Variable to store unique characters

for char in text:                           # Loop through each character
    if char not in result:                  # Check if character already exists
        result += char                      # Add unique character to result

print("String without duplicates:", result) # Display result

# Output Example
# Enter a string: programming
# String without duplicates: progamin
