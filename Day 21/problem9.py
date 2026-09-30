def remove_duplicates(nums):
    seen = set()
    for num in nums:
        if num not in seen:
            seen.add(num)
    return seen

nums = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(nums))