#Function to flatten a nested list
def flatten_list(nested_list):
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))  # Recursive call
        else:
            result.append(item)

    return result


# Input
data = [1, [2, 3], [4, [5, 6]], 7]

# Output
flattened = flatten_list(data)

print("Flattened list:", flattened)

#output
#Flattened list: [1, 2, 3, 4, 5, 6, 7]
