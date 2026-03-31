# Function to find first non-repeating character
def first_non_repeating_char(s):
    freq = {}

    # Count frequency of each character
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Find first non-repeating character
    for char in s:
        if freq[char] == 1:
            return char

    return None


# Input
text = "aabbcdeff"

# Output
result = first_non_repeating_char(text)

print("First non-repeating character:", result)

#output
#First non-repeating character: c
