# Program to find the sum of even numbers up to N

n = int(input("Enter value of N: "))   # Take value of N from the user
i = 1                                  # Initialize counter variable
sum_even = 0                           # Variable to store sum of even numbers

while i <= n:                          # Loop runs from 1 to N
    if i % 2 == 0:                     # Check if the number is even
        sum_even = sum_even + i        # Add even number to sum
    i = i + 1                          # Increase counter by 1

print("Sum of even numbers:", sum_even) # Display the final sum

# Output Example
# Enter value of N: 10
# Sum of even numbers: 30
