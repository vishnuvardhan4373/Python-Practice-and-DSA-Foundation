def most_frequent(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num,0) + 1
    most_frequent = max(frequency, key = frequency.get)
    return most_frequent

nums = [1, 3, 2, 3, 4, 3, 2]
print(most_frequent(nums))