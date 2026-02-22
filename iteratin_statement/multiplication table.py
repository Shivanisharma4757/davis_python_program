# Program to print the multiplication table of a given number

# Take input from the user
num = int(input("Enter a number: "))

# Take the range of the multiplication table
limit = int(input("Enter the range of the table: "))

print(f"Multiplication table of {num} up to {limit}:")

# Loop to print the table
for i in range(1, limit + 1):
    result = num * i
    print(f"{num} x {i} = {result}")
