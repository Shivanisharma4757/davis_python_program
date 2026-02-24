# Program to count vowels in a string

text = input("Enter a string: ")       # Take string input from user
count = 0                              # Initialize vowel counter

for char in text:                      # Loop through each character in string
    if char.lower() in "aeiou":        # Check if character is a vowel
        count = count + 1              # Increase vowel count

print("Number of vowels:", count)      # Display total vowels

# Output Example
# Enter a string: hello
# Number of vowels: 2
