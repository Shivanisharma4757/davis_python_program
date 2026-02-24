# Program to find key with maximum value in dictionary

data = {"A": 10, "B": 45, "C": 23, "D": 67}   # Create dictionary with key-value pairs

max_key = ""                                  # Variable to store key with maximum value
max_value = 0                                 # Variable to store maximum value

for key in data:                              # Loop through dictionary keys
    if data[key] > max_value:                  # Check if current value is greater than max_value
        max_value = data[key]                  # Update max_value
        max_key = key                          # Update key having maximum value

print("Key with maximum value:", max_key)     # Display key with highest value
print("Maximum value:", max_value)            # Display maximum value

# Output Example
# Key with maximum value: D
# Maximum value: 67
