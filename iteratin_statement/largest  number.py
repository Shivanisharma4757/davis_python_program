# Program to find the largest number in a list using a loop

# Example list (you can also take input from user)
numbers = [12, 45, 2, 89, 33, 77]

# Assume the first element is the largest
largest = numbers[0]

# Loop through the list to compare each number
for num in numbers:
    if num > largest:
        largest = num  # Update largest if current number is greater

# Display the largest number
print("The largest number in the list is:", largest)
#output
#The largest number in the list is: 89
