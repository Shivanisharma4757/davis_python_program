# Program to check whether two strings are anagrams

str1 = input("Enter first string: ")        # Take first string input
str2 = input("Enter second string: ")       # Take second string input

str1 = str1.replace(" ", "").lower()        # Remove spaces and convert to lowercase
str2 = str2.replace(" ", "").lower()        # Remove spaces and convert to lowercase

if sorted(str1) == sorted(str2):            # Compare sorted characters of both strings
    print("Strings are anagrams")           # Display if anagram
else:                                       # Otherwise
    print("Strings are not anagrams")       # Display if not anagram

# Output Example
# Enter first string: listen
# Enter second string: silent
# Strings are anagrams
