# Program to check whether a number is palindrome or not

# Take input from the user
num = int(input("Enter a number: "))

# Store original number
original = num

# Initialize reverse number
reverse = 0

# Reverse the number using while loop
while num > 0:
    digit = num % 10          # Get last digit
    reverse = reverse * 10 + digit
    num = num // 10           # Remove last digit

# Check if original and reversed numbers are equal
if original == reverse:
    print(original, "is a palindrome number")
else:
    print(original, "is not a palindrome number")
#output
#Enter a number: 121
#121 is a palindrome number
