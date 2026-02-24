# Program to print multiplication table of a number using while loop

num = int(input("Enter a number: "))   # Take number input from user
i = 1                                  # Initialize counter

while i <= 10:                         # Loop runs from 1 to 10
    print(num, "x", i, "=", num*i)     # Print multiplication result
    i = i + 1                          # Increase counter

# Output Example
# Enter a number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
