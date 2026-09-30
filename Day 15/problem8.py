def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest
nums = [10, 4, 25, 7, 18]
print(find_largest(nums))