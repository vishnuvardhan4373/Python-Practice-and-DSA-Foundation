def first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

nums = [5, 3, 4, 2, 3, 5]
print(first_duplicate(nums))