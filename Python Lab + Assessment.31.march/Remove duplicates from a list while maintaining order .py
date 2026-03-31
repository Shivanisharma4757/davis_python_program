# Function to remove duplicates while maintaining order
def remove_duplicates(lst):
    seen = []
    
    for item in lst:
        if item not in seen:
            seen.append(item)
    
    return seen


# Input
numbers = [1, 2, 2, 3, 4, 3, 5, 1]

# Output
result = remove_duplicates(numbers)

print("List without duplicates:", result)

#output
#List without duplicates: [1, 2, 3, 4, 5]
