values = [5, 2, 8]

stack = []
min_stack = []

def push(values_list):
    for value in values_list:
        stack.append(value)
        # If min_stack is empty, or the new value is smaller than/equal to current min
        if not min_stack or value <= min_stack[-1]:
            min_stack.append(value)

def pop():
    if not stack:
        return None
    removed = stack.pop()
    # If the number we are removing is the current minimum, pop it from min_stack too
    if removed == min_stack[-1]:
        min_stack.pop()
    return removed

def get_min():
    if not min_stack:
        return None
    return min_stack[-1]

# Test it out
push(values)
print("Stack:", stack)          # [5, 2, 8]
print("Min Stack:", min_stack)  # [5, 2]
print("Current Min:", get_min()) # 2