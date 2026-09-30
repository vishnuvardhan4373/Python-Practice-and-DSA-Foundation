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
        break
    return nums

nums = [7, 2, 9, 4, 1]
print(bubble_sort(nums))