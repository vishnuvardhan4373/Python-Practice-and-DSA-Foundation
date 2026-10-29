def next_greater(nums):
    res = [-1] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            j = stack.pop()
            res[j] = nums[i]
        stack.append(i)
    return res

nums = [4, 5, 2, 10, 8]
print(next_greater(nums))