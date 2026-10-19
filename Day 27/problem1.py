nums = [1, 2, 3, 4, 5]
stack = []
rev_stack = []
for num in nums:
    stack.append(num)
print(stack)
for num in nums:
    removed = stack.pop()
    rev_stack.append(removed)
print(rev_stack)