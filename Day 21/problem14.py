def longest_consecutive(nums):
    new_nums = set(nums)
    longest_streak = 0

    for num in new_nums:
        if (num - 1) not in new_nums:
            current_num = num
            current_streak = 1
            while(current_num + 1) in new_nums:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak

nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))