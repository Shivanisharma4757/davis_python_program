# Program to find most frequent character in string

text = input("Enter a string: ")            # Take string input

freq = {}                                   # Create empty dictionary

for char in text:                           # Loop through characters
    if char in freq:                        # Check if character already exists
        freq[char] += 1                     # Increase frequency
    else:                                   # Otherwise
        freq[char] = 1                      # Initialize frequency

max_char = max(freq, key=freq.get)          # Find character with highest frequency

print("Most frequent character:", max_char) # Display result
print("Frequency:", freq[max_char])         # Display frequency

# Output Example
# Enter a string: programming
# Most frequent character: r
# Frequency: 2
