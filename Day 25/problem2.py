def array_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

nums = [1, 2, 3, 4, 5]
print(array_sum(nums))