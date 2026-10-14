nums = [10, -5, 0, 20, -2, 0, 7]
positive_numbers = 0
negative_numbers = 0
zeros = 0
for num in nums:
    if num > 0:
        positive_numbers += 1
    elif num < 0:
        negative_numbers += 1
    else:
        zeros += 1
print(positive_numbers)
print(negative_numbers)
print(zeros)