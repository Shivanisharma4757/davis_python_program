# Program to count vowels in a string using a function

def count_vowels(text):                   # Define function to count vowels
    count = 0                             # Initialize vowel counter
    
    for char in text:                     # Loop through each character
        if char.lower() in "aeiou":       # Check if character is vowel
            count = count + 1             # Increase vowel count
    
    return count                          # Return vowel count


string = input("Enter a string: ")        # Take string input from user

result = count_vowels(string)             # Call function

print("Number of vowels:", result)        # Display result

# Output Example
# Enter a string: hello
# Number of vowels: 2
