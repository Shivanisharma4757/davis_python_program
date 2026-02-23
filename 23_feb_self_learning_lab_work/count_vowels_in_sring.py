# Program to count the number of vowels in a string

# Taking input from the user
text = input("Enter a string: ")

# Initialize vowel counter
vowel_count = 0

# Define vowels
vowels = "aeiouAEIOU"

# Loop through each character in the string
for char in text:
    if char in vowels:
        vowel_count += 1   # Increase counter if character is a vowel

# Display the result
print("Number of vowels in the string:", vowel_count)

# output
# Enter a string: Hello World
# Number of vowels in the string: 3
