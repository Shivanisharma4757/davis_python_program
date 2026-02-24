# Program to generate Fibonacci series using for loop

n = int(input("Enter number of terms: "))  # Take number of terms from user
a = 0                                      # First Fibonacci number
b = 1                                      # Second Fibonacci number

for i in range(n):                         # Loop runs n times
    print(a)                               # Print current Fibonacci number
    c = a + b                              # Calculate next number
    a = b                                  # Update first number
    b = c                                  # Update second number

# Output Example
# Enter number of terms: 6
# 0
# 1
# 1
# 2
# 3
# 5
