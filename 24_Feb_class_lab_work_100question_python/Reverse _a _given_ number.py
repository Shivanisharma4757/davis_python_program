# Problem 10
# Program to reverse a given number

# Taking input from the user
num = int(input("Enter a number: "))

# Store original sign
sign = -1 if num < 0 else 1
num = abs(num)

# Initialize reverse variable
reverse = 0

# Reversing the number
while num > 0:
    digit = num % 10          # Extract last digit
    reverse = reverse * 10 + digit
    num //= 10                # Remove last digit

# Restore original sign
reverse *= sign

# Print the result
print("Reversed number is:", reverse)

#output
#Enter a number: 7895
#Reversed number is: 5987
