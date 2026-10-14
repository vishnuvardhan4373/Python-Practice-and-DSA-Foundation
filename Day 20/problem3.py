def count_windows(nums,k):
    windows_count = len(nums) - k + 1
    return windows_count
nums = [1, 2, 3, 4, 5]
print(count_windows(nums,3))