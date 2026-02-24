# Program to find maximum of three numbers using function

def find_max(a, b, c):                      # Define function to find maximum
    if a >= b and a >= c:                   # Check if a is largest
        return a                            # Return a
    elif b >= a and b >= c:                 # Check if b is largest
        return b                            # Return b
    else:                                   # Otherwise
        return c                            # Return c


x = int(input("Enter first number: "))     # Take first number input
y = int(input("Enter second number: "))    # Take second number input
z = int(input("Enter third number: "))     # Take third number input

largest = find_max(x, y, z)                # Call function to find maximum

print("Largest number is:", largest)       # Display largest number


# Output Example
# Enter first number: 10
# Enter second number: 25
# Enter third number: 15
# Largest number is: 25
