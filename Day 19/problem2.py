def two_sum(nums,target):
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

nums = [1, 2, 3, 4, 6]
print(two_sum(nums,6))