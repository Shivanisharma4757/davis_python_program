# Program to demonstrate isalpha() and isalnum() string methods in Python

# Assigning a string containing alphabets and a space
sentence = "hello world"

# isalpha() returns True only if all characters are alphabets (no spaces, digits, or special characters)
print(sentence.isalpha())    # False because space is present


# Assigning a string containing only alphabets
str2 = "hello"

# Checking whether the string contains only alphabets
print(str2.isalpha())        # True


# Assigning a string containing alphabets, space, and digits
str3 = "hello 123"

# isalnum() returns True only if all characters are letters or digits (no spaces or special characters)
print(str3.isalnum())        # False because space is present


# Assigning a string containing only digits
str4 = "123"

# Checking whether the string contains only alphanumeric characters
print(str4.isalnum())        # True

#output
#False
#True
#False
#True
