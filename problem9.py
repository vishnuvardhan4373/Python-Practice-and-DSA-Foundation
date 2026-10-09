def remove_duplicates(nums):
    slow = 0
    for fast in range(0,len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow], nums[fast] = nums[fast], nums[slow]    
    return nums[:slow+1]

nums = [1, 1, 2, 2, 3, 4, 4]
print(remove_duplicates(nums))