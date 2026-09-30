def find_max(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

nums = [5, 2, 7, 2, 9, 2]
print(f"Maximum Number in the list is: {find_max(nums)}.")