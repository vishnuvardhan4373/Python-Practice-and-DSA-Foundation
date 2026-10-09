nums = [1, 2, 3, 4, 5, 6]
def even_nums(nums):
    
    result = list(filter(lambda x: x % 2 == 0, nums))
    return result

print(even_nums(nums))