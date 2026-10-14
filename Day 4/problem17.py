def palindrome(n):
    reversed_number = 0
    original = n
    
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10
    
    is_palindrome = (original == reversed_number)
    return is_palindrome


n = int(input("Enter number: "))
print(palindrome(n))