def find_min(nums):
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest

nums = [5, 2, 7, 2, 9, 2]
print(f"Maximum Number in the list is: {find_min(nums)}.")