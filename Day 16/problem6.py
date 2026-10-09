def is_even(n):
    return n %2 == 0
def is_poitive(n):
    return n > 0
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def square(n):
    return n*n

def analyze_number(n):
    result1 = is_even(n)
    result2 = is_poitive(n)
    result3 = is_prime(n)
    result4 = square(n)
    return result1, result2, result3, result4

n = 36
print(analyze_number(n))