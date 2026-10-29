from collections import deque
def generate_binary(n):
    queue = deque(["1"])
    res = []
    for _ in range(n):
        current = queue.popleft()
        res.append(current)
        queue.append(current + "0")
        queue.append(current + "1")
    return res

n = 5
print(generate_binary(n))