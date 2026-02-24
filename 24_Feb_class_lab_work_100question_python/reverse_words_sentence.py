# Program to reverse words in a sentence

text = input("Enter a sentence: ")          # Take sentence input

words = text.split()                        # Split sentence into words

reversed_words = words[::-1]                # Reverse list of words

result = " ".join(reversed_words)           # Join words back into sentence

print("Reversed sentence:", result)         # Display reversed sentence

# Output Example
# Enter a sentence: python is fun
# Reversed sentence: fun is python
