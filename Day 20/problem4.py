def min_sum_of_consecutive_nums(nums,k):
    windows_sum = sum(nums[:k])
    min_sum = windows_sum

    for i in range(k,len(nums)):
        windows_sum = windows_sum - nums[i - k] + nums[i]

        if windows_sum < min_sum:
            min_sum = windows_sum
    return min_sum
nums = [4, 2, 1, 7, 8, 1, 2]
print(min_sum_of_consecutive_nums(nums,3))