nums = [1, 2, 3, 5, 6]
full_set = set(range(1, 7))
nums_set = set(nums)
missing_number = full_set - nums_set
print(missing_number)