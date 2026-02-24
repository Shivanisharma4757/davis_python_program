# Problem 9
# Program to find the sum of digits of a number

# Taking input from the user
num = int(input("Enter a number: "))

# Making the number positive (in case of negative input)
num = abs(num)

# Initializing sum variable
digit_sum = 0

# Calculating sum of digits
while num > 0:
    digit = num % 10        # Extract last digit
    digit_sum += digit      # Add digit to sum
    num //= 10              # Remove last digit

# Printing the result
print("Sum of digits is:", digit_sum)

#output
#Enter a number: 4567
#Sum of digits is: 22
