def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [10, 20, 30, 40, 50]
print(f"Element found at Index: {linear_search(nums,30)}")