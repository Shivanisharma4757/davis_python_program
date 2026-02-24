# Program to find GCD (Greatest Common Divisor) using while loop

a = int(input("Enter first number: "))   # Take first number from user
b = int(input("Enter second number: "))  # Take second number from user

while b != 0:                            # Loop runs until second number becomes 0
    temp = b                             # Store value of b
    b = a % b                            # Update b with remainder
    a = temp                             # Update a with previous b

print("GCD is:", a)                      # Display the GCD

# Output Example
# Enter first number: 12
# Enter second number: 18
# GCD is: 6
