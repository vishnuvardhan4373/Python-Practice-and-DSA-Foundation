def bubble_sort(nums):
    n = len(nums)
    swap_count = 0
    comparisions = 0

    for i in range(n-1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j+1]:
                swapped = True
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap_count += 1
            comparisions += 1
        if not swapped:
            break
    return nums, swap_count, comparisions

nums = [5, 1, 4, 2, 8]
print(bubble_sort(nums))