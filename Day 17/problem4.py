nums = [5, 2, 7, 2, 9, 2]
target = 2
result = []
for i in range(len(nums)):
    if nums[i] == target:
        result.append(i)
print(result)