nums = [5, 2, 1, 8]
result = []
left = 0
right = left + 1
while left <= right:
    if nums[left] > nums[right]:
        left, right = right, left
        left += 1
        right += 1
        result.append(nums)
print(result)
