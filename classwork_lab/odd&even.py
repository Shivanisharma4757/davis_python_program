# Python Program to Check Odd or Even

# Step 1: Take input from the user
num = int(input("Enter a number: "))  # Convert input to integer

# Step 2: Check if the number is divisible by 2
if num % 2 == 0:  # '%' gives the remainder. If remainder is 0, the number is even
    print(f"{num} is Even")  # Number is even
else:
    print(f"{num} is Odd")   # Otherwise, number is odd

output
Enter a number: 7
7 is Odd

output
Enter a number: 12
12 is Even
