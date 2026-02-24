# Program to perform simple string compression

text = input("Enter a string: ")          # Take string input

compressed = ""                           # Variable to store compressed string
count = 1                                 # Counter for repeating characters

for i in range(len(text) - 1):            # Loop through string characters
    if text[i] == text[i + 1]:            # Check if next character is same
        count += 1                        # Increase count
    else:                                 # If character changes
        compressed += text[i] + str(count) # Add character and count to result
        count = 1                         # Reset counter

compressed += text[-1] + str(count)       # Add last character and its count

print("Compressed string:", compressed)   # Display compressed string

# Output Example
# Enter a string: aaabbc
# Compressed string: a3b2c1
