def analyze_number(n):
    digit_count = 0
    digit_sum = 0
    reverse_number = 0
    original = n
    largest_digit = 0
    
    while n > 0:
        digit = n % 10
        digit_sum += digit
        digit_count += 1
        reverse_number = reverse_number * 10 + digit
        if digit > largest_digit:
            largest_digit = digit
        n = n // 10
    is_palindrome = (original == reverse_number)
    return (digit_count, digit_sum, largest_digit, is_palindrome)

print(analyze_number(23578))