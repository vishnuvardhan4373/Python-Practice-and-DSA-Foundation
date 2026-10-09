def bubble_sort(nums):
    n = len(nums)
    new_nums = nums[0:n+1]
    m = len(new_nums)
    for i in range(m - 1):
        swapped = False
        for j in range(n - i - 1):
            if new_nums[j] > new_nums[j+1]:
                swapped = True
                new_nums[j], new_nums[j+1] = new_nums[j+1], new_nums[j]
        if not swapped:
            break
    return nums, new_nums

nums = [5, 2, 8, 1, 3]
print(bubble_sort(nums))