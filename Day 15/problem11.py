nums = [1, 2, 3, 4, 5]
def square_nums(nums):
    
    result = list(map(lambda x: x * x, nums))
    return result

print(square_nums(nums))