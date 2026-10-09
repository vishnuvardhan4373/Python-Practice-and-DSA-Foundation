def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
def display_result(n):
    result = check_number(n)
    return result
print(display_result(9))
print(display_result(-6))
print(display_result(0))