def is_even(n):
    return n %2 == 0
def square(n):
    return n * n
def analyze_number(n):
    result1 = is_even(n)
    result2 = square(n)
    return result1,result2
print(analyze_number(6))