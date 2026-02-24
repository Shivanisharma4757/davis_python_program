# Program to count number of words in a string

text = input("Enter a sentence: ")      # Take sentence input

words = text.split()                    # Split sentence into words

count = len(words)                      # Count number of words

print("Number of words:", count)        # Display word count

# Output Example
# Enter a sentence: Python is easy to learn
# Number of words: 5
