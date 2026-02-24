# Program to find factorial of a number using while loop

num = int(input("Enter a number: "))   # Take number input from user
fact = 1                               # Initialize factorial variable with 1
i = 1                                  # Initialize counter variable

while i <= num:                        # Loop will run until i reaches the number
    fact = fact * i                    # Multiply fact with current value of i
    i = i + 1                          # Increase i by 1

print("Factorial is:", fact)           # Display the factorial result

# Output Example
# Enter a number: 5
# Factorial is: 120
