# Program to find the average of list elements

numbers = [10, 20, 30, 40]               # Create a list of numbers

total = 0                                # Initialize sum variable

for num in numbers:                      # Loop through each element
    total = total + num                  # Add number to total

average = total / len(numbers)           # Calculate average

print("Average:", average)               # Display average value

# Output Example
# Average: 25.0
