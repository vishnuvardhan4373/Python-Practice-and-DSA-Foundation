def frequency_count(nums):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num,0) + 1
    return frequency

nums = [1, 2, 2, 3, 3, 3, 4]
print(frequency_count(nums))