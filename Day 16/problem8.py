def even_count(nums):
    even_count = 0
    for num in nums:
        if num %2 == 0:
            even_count += 1
    return even_count
def odd_count(nums):
    odd_count = len(nums) - even_count(nums)
    return odd_count
def analyze_list(nums):
    result1 = even_count(nums)
    result2 = odd_count(nums)
    return result1, result2

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(analyze_list(nums))
            