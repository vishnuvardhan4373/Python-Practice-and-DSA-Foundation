def second_largest(nums):
    largest = nums[0]
    Second_largest = nums[1]
    for num in nums:
        if num > largest:
            Second_largest = largest
            largest = num
        elif num > Second_largest and num != largest:
            Second_largest = num
    return Second_largest

nums = [10, 5, 20, 8, 20, 15]
print(second_largest(nums))