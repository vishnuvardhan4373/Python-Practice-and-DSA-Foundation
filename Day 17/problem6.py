def count_occurrences(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count
nums = [1, 2, 2, 3, 2, 4]
print(count_occurrences(nums,2))