def bubble_sort(nums):
    n = len(nums)
    swap_count = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap_count += 1
    return nums, swap_count

nums = [5, 3, 8, 1, 2]
print(bubble_sort(nums))