def binary_search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        middle = (left + right) // 2

        if nums[middle] == target:
            return middle

        elif nums[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1

nums = [10, 20, 30, 40, 50, 60, 70]
print(binary_search(nums,50))