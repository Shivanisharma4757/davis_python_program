# Program to find factorial using a function

def factorial(num):                         # Define function to calculate factorial
    fact = 1                                # Initialize factorial variable
    
    for i in range(1, num + 1):              # Loop from 1 to the given number
        fact = fact * i                      # Multiply factorial with i
    
    return fact                              # Return the factorial value


number = int(input("Enter a number: "))     # Take number input from user

result = factorial(number)                  # Call factorial function

print("Factorial is:", result)              # Display the result


# Output Example
# Enter a number: 5
# Factorial is: 120
