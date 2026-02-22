# Program to print Fibonacci series using a loop

# Take number of terms from user
n = int(input("Enter number of terms: "))

# First two Fibonacci numbers
first = 0
second = 1

# Check if input is valid
if n <= 0:
    print("Please enter a positive number")

else:
    print("Fibonacci Series:")

    # Loop to generate Fibonacci series
    for i in range(n):
        print(first, end=" ")

        # Update values
        next_term = first + second
        first = second
        second = next_term
