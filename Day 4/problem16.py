def reverse_number(n):
    reversed_number = 0
    
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10
    
    return reversed_number


result = reverse_number(58372)
print(result)