def count_frequency(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency
nums = [1, 2, 2, 3, 1, 1, 4]
print(count_frequency(nums))            