stack1 = []
stack2 = []
def enqueue(values):
    for value in values:
        stack1.append(value)
def dequeue():
    if len(stack2) == 0:
        while len(stack1) != 0:
            j = stack1.pop()
            stack2.append(j)
    if len(stack2) == 0:
        return None
    return stack2.pop()
values = [10, 20, 30]
enqueue(values)
print(dequeue())