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
#output
#Enter a number: 5
#Enter the range of the table: 10
#Multiplication table of 5 up to 10:
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35
#5 x 8 = 40
#5 x 9 = 45
#5 x 10 = 50
