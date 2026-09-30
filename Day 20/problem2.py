def average_of_consecutive_nums(nums,k):
    windows_sum = sum(nums[:k])
    average_of_nums = windows_sum / len(nums[:k])
    max_average = average_of_nums
    for i in range(k,len(nums)):
        windows_sum = windows_sum - nums[i - k] + nums[i]
        average_of_nums = windows_sum / len(nums[i-k:i])

        if average_of_nums > max_average:
            max_average = average_of_nums
    return max_average
nums = [1, 12, -5, -6, 50, 3]
print(average_of_consecutive_nums(nums,4))