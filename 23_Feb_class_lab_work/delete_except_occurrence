# Step 1: Create a list of 20 numbers
numbers = [5, 10, 15, 10, 20, 25, 10, 30, 35, 10,
           40, 45, 10, 50, 55, 10, 60, 65, 10, 70]

# Step 2: Take input from user
num = int(input("Enter a number to delete its occurrences: "))

# Step 3: Check if number exists in the list
if num in numbers:
    first_index = numbers.index(num)   # Index of first occurrence

    # Remove all other occurrences
    i = first_index + 1
    while i < len(numbers):
        if numbers[i] == num:
            numbers.pop(i)
        else:
            i += 1

    print("Updated list:", numbers)
else:
    print("Number not found in the list.")

  # output
  # Enter a number to delete its occurrences: 10
  # Updated list: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
