def find_max(nums):
    maximum = nums[0]
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum

nums = [4, 8, 2, 10, 5]
print(find_max(nums))