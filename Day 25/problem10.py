def second_largest(nums):
    largest = nums[0]
    second_largest = nums[1]
    slow = 0
    for fast in range(0,len(nums)):
        if nums[fast] > nums[slow]:
            second_largest = largest
            largest = nums[fast]
            slow += 1
        elif nums[fast] > second_largest and nums[fast] != largest:
            second_largest = nums[fast]
    return second_largest
    
nums = [10, 5, 8, 10, 3]
print(second_largest(nums))