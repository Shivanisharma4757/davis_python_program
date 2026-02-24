# Program to count uppercase and lowercase letters

text = input("Enter a string: ")            # Take string input

upper = 0                                   # Variable to count uppercase letters
lower = 0                                   # Variable to count lowercase letters

for char in text:                           # Loop through characters
    if char.isupper():                      # Check if character is uppercase
        upper += 1                          # Increase uppercase count
    elif char.islower():                    # Check if character is lowercase
        lower += 1                          # Increase lowercase count

print("Uppercase letters:", upper)          # Display uppercase count
print("Lowercase letters:", lower)          # Display lowercase count

# Output Example
# Enter a string: PyThOn
# Uppercase letters: 3
# Lowercase letters: 3
