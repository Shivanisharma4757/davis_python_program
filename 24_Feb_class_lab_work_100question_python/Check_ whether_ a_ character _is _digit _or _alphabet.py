# Problem 14
# Program to check whether a character is digit or alphabet

# Taking input from the user
ch = input("Enter a character: ")

# Checking if input is a single character
if len(ch) == 1:
    if ch.isdigit():
        print("The character is a Digit")
    elif ch.isalpha():
        print("The character is an Alphabet")
    else:
        print("The character is neither a Digit nor an Alphabet")
else:
    print("Invalid input. Please enter a single character.")

#output
#Enter a character: 5
#The character is a Digit
