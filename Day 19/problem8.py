def unique_pairs(nums, target):
    left = 0
    right = len(nums) - 1
    result = []

    while left < right:
        total = nums[left] + nums[right]

        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            result.append((nums[left],nums[right]))
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
    return result

nums = [1, 1, 2, 2, 3, 4, 4, 5]
print(unique_pairs(nums,6))            