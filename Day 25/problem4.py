def count_even(nums):
    even_count = 0
    for num in nums:
        if num %2 == 0:
            even_count += 1
    return even_count

nums = [1, 2, 4, 7, 8, 11]
print(count_even(nums))