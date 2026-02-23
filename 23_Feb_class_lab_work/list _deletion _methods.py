# ------------------------------------------
# Program to demonstrate list deletion methods
# ------------------------------------------

# Create a list of 10 elements with repeated numbers
number = [45, 67, 89, 45, 23, 67, 89, 45, 23, 67]

# Displaying the original list
print("The list is:")
print(number)
print("---------------------------------------")

# Delete the element at index 5 using pop(index)
number.pop(5)
print("The list after deleting the element at index 5 is:")
print(number)

# Delete the last element using pop() without index
number.pop()
print("The list after deleting the last element is:")
print(number)

print("---------------------------------------")

# Delete the first occurrence of 45 using remove(value)
number.remove(45)
print("The list after deleting the first occurrence of 45 is:")
print(number)

#output
#The list is:
#[45, 67, 89, 45, 23, 67, 89, 45, 23, 67]
#---------------------------------------
#The list after deleting the element at index 5 is:
#[45, 67, 89, 45, 23, 89, 45, 23, 67]
#The list after deleting the last element is:
#[45, 67, 89, 45, 23, 89, 45, 23]
#---------------------------------------
#The list after deleting the first occurrence of 45 is:
#[67, 89, 45, 23, 89, 45, 23]
