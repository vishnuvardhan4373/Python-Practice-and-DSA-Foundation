def rotating_array(nums,k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
print(rotating_array(nums,3))