# Problem 13
# Program to check whether a character is vowel or consonant

# Taking input from the user
ch = input("Enter a character: ")

# Convert to lowercase to handle uppercase inputs
ch = ch.lower()

# Checking if input is a single alphabet
if len(ch) == 1 and ch.isalpha():
    if ch in ('a', 'e', 'i', 'o', 'u'):
        print("The character is a Vowel")
    else:
        print("The character is a Consonant")
else:
    print("Invalid input. Please enter a single alphabet.")

#output
#Enter a character: A
#The character is a Vowel
#Enter a character: D
#The character is a Consonant
