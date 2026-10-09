def bubble_sort(nums):
    n = len(nums)
    for j in range(n-1):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [7, 2, 9, 4, 1]
print(bubble_sort(nums))