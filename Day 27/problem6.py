from collections import deque
queue = deque([1, 2, 3, 4, 5])
k = 3
stack = []
for i in range(k):
    stack.append(queue[i])
for i in range(k):
    queue.popleft()
res = deque()
for i in range(len(stack)):
    res.append(stack.pop())
for i in range(len(queue)):
    res.append(queue.popleft())
print(res)