def bubble_sort(nums):
    n = len(nums)
    passes = 0
    for i in range(n-1):
        swapped = False
        passes += 1
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                swapped = True
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if not swapped:
            break
    return nums, passes

nums = [5, 4, 3, 2, 1]
print(bubble_sort(nums))