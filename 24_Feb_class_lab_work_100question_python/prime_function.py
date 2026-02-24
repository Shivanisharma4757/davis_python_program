# Program to check whether a number is prime using a function

def check_prime(num):                       # Define a function to check prime number
    if num <= 1:                            # Check if number is less than or equal to 1
        return False                        # Numbers <=1 are not prime
    
    for i in range(2, num):                 # Loop from 2 to num-1
        if num % i == 0:                    # Check if number is divisible
            return False                    # If divisible, it is not prime
    
    return True                             # If no divisor found, number is prime


number = int(input("Enter a number: "))     # Take number input from user

if check_prime(number):                     # Call the function to check prime
    print("Prime Number")                   # Print if number is prime
else:                                       # Otherwise
    print("Not a Prime Number")             # Print if number is not prime


# Output Example
# Enter a number: 7
# Prime Number
