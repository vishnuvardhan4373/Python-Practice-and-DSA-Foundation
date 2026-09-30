def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                swapped = True
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if not swapped:
            break
    return nums

nums = [5, 3, 1, 4, 2]
print(bubble_sort(nums))