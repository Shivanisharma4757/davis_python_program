# Program to print all divisors of a number

num = int(input("Enter a number: "))      # Take number input from the user

for i in range(1, num + 1):               # Loop from 1 to the given number
    if num % i == 0:                      # Check if i divides the number exactly
        print(i)                          # Print the divisor

# Output Example
# Enter a number: 12
# 1
# 2
# 3
# 4
# 6
# 12
