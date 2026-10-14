def remove_duplicates(nums):
    unique_numbers = set(nums)
    return unique_numbers
nums = [1, 2, 2, 3, 4, 3, 5, 1]
print(remove_duplicates(nums))