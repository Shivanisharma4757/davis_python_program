# Program to calculate power using recursive function

def power(base, exp):                     # Define recursive function
    if exp == 0:                          # Base case
        return 1                          # Any number power 0 is 1
    else:                                 # Recursive case
        return base * power(base, exp-1)  # Multiply base recursively


base = int(input("Enter base: "))         # Take base input from user
exponent = int(input("Enter exponent: ")) # Take exponent input from user

result = power(base, exponent)            # Call recursive function

print("Result:", result)                  # Display power result

# Output Example
# Enter base: 2
# Enter exponent: 4
# Result: 16
