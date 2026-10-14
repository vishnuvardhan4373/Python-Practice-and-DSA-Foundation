def move_zeros(nums):
    if not nums:
        return []
    slow  = 0
    for fast in range(1,len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums
nums = [0, 1, 0, 3, 12]
print(move_zeros(nums))