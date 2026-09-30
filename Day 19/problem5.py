def two_sum(nums,target):
    left = 0
    right = len(nums) - 1

    while left < right:
        total = abs(nums[left] - nums[right])

        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False

nums = [1, 3, 5, 7, 9]
print(two_sum(nums,4))