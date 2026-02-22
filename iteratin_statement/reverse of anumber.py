# Program to find the reverse of a number using a while loop

# Take input from the user
num = int(input("Enter a number: "))

# Store original number (optional, for display purposes)
original = num

# Initialize variable to store reversed number
reverse = 0

# Loop until the number becomes 0
while num > 0:
    digit = num % 10          # Get the last digit
    reverse = reverse * 10 + digit  # Append digit to reverse
    num = num // 10           # Remove the last digit

# Display the reversed number
print("Reverse of", original, "is", reverse)
