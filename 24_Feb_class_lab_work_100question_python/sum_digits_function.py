# Program to find sum of digits using function

def sum_digits(num):                        # Define function to calculate sum of digits
    total = 0                               # Initialize total variable
    
    while num > 0:                          # Loop until number becomes 0
        digit = num % 10                    # Extract last digit
        total = total + digit               # Add digit to total
        num = num // 10                     # Remove last digit
    
    return total                            # Return total sum


number = int(input("Enter a number: "))    # Take number input from user

result = sum_digits(number)                # Call function

print("Sum of digits:", result)            # Display result


# Output Example
# Enter a number: 123
# Sum of digits: 6
