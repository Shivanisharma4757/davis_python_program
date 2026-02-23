# -----------------------------------
# List Functions in Python
# -----------------------------------
# count(x)   -> Returns the number of times x appears in the list
# reverse()  -> Reverses the order of the list
# remove(x)  -> Removes the first occurrence of x from the list

# Create an empty list
numbers = []

# Take 20 numbers from the user
print("Enter 20 numbers:")
for i in range(20):
    num = int(input())
    numbers.append(num)

print("--------------------------------")

# Display the original list
print("List is:")
print(numbers)
print("--------------------------------")

# Ask the user which number to remove
remove_num = int(input("Enter a number to remove from the list: "))

# Count frequency of the number
frequency = numbers.count(remove_num)

# Case 1: Number not present
if frequency == 0:
    print("The number you entered is not in the list.")

# Case 2: Number appears only once (unique)
elif frequency == 1:
    print("The number appears only once, so it cannot be removed.")

# Case 3: Number appears more than once
else:
    # Remove duplicate occurrences but keep one copy
    for i in range(frequency - 1):
        numbers.remove(remove_num)

    print("Duplicates removed successfully.")

print("--------------------------------")
print("The list after removing", remove_num, "is:")
print(numbers)

#output
#Enter 20 numbers:
#7
#9
#7
#6
#6
#4
#4
#5
#6
#6
#8
#4
#4
#5
#3
#3
#5
#5
#3
#4
#--------------------------------
#List is:
#[7, 9, 7, 6, 6, 4, 4, 5, 6, 6, 8, 4, 4, 5, 3, 3, 5, 5, 3, 4]
#--------------------------------
#Enter a number to remove from the list: 7
#Duplicates removed successfully.
#--------------------------------
#The list after removing 7 is:
#[7, 9, 6, 6, 4, 4, 5, 6, 6, 8, 4, 4, 5, 3, 3, 5, 5, 3, 4]
