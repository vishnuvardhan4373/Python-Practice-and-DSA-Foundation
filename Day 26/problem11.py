def missing_number(nums):
    n = len(nums)
    return n * (n+1) // 2 - sum(nums)
    
nums = [3, 0, 1]
print(missing_number(nums))