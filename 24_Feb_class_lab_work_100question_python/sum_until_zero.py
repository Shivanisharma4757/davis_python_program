# Program to accept numbers until 0 is entered and then print their sum

total = 0                                # Variable to store total sum

while True:                              # Infinite loop
    num = int(input("Enter number (0 to stop): "))  # Take number from user
    
    if num == 0:                         # Check if user entered 0
        break                            # Exit the loop
    
    total = total + num                  # Add number to total sum

print("Total Sum:", total)               # Display final sum

# Output Example
# Enter number (0 to stop): 5
# Enter number (0 to stop): 3
# Enter number (0 to stop): 2
# Enter number (0 to stop): 0
# Total Sum: 10
