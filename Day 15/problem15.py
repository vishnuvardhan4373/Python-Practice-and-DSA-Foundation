def second_largest(nums):
    largest = nums[0]
    second_largest = nums[1]
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest
nums = [10, 5, 20, 8, 20, 15]
print(second_largest(nums))