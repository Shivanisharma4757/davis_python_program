# Program to merge two dictionaries manually

dict1 = {"a": 1, "b": 2}                # Create first dictionary
dict2 = {"c": 3, "d": 4}                # Create second dictionary

merged = {}                             # Create empty dictionary

for key in dict1:                       # Loop through first dictionary
    merged[key] = dict1[key]            # Add elements to merged dictionary

for key in dict2:                       # Loop through second dictionary
    merged[key] = dict2[key]            # Add elements to merged dictionary

print("Merged dictionary:", merged)     # Display merged dictionary

# Output Example
# Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
