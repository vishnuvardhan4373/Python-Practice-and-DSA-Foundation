nums = [10, 20, 5, 30, 25]
largest = nums[0]
second_largest = nums[1]
for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(largest)
print(second_largest)