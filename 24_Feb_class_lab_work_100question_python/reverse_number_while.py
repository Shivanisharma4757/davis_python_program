# Program to reverse a number using while loop

num = int(input("Enter a number: "))   # Take number input from user
reverse = 0                            # Initialize variable to store reversed number

while num > 0:                         # Loop will run while number is greater than 0
    digit = num % 10                   # Extract the last digit of the number
    reverse = reverse * 10 + digit     # Add the digit to the reversed number
    num = num // 10                    # Remove the last digit from the number

print("Reversed number:", reverse)     # Display the reversed number

# Output Example
# Enter a number: 1234
# Reversed number: 4321
