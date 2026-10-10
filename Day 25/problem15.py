def move_negative_numbers(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] < 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

nums = [3, -1, 4, -2, 0, -5, 2]
print(move_negative_numbers(nums))