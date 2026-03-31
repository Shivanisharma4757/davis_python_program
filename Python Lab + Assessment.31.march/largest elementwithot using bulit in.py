def second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements

    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None  # No second largest (e.g., all elements same)

    return second_largest


# Example
data = [10, 20, 4, 45, 99]
print(second_largest(data))

#outut
#45
