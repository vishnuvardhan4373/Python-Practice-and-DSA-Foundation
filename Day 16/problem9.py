def reversed_number(n):
    reversed_number = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10
    return reversed_number
def is_palindrome(n):
    if n == reversed_number(n):
        return True
    return False
n = 12321
print(reversed_number(n))
print(is_palindrome(n))