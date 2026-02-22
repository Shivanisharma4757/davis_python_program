# Program to print Armstrong numbers between 1 and 1000

# Loop through numbers from 1 to 1000
for num in range(1, 1001):
    
    # Store original number
    original = num
    sum_of_powers = 0
    
    # Count number of digits
    digits = len(str(num))
    
    # Temporary variable to calculate sum
    temp = num
    
    # Calculate sum of digits raised to the power of number of digits
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** digits
        temp = temp // 10
    
    # Check if number is Armstrong
    if original == sum_of_powers:
        print(original)
