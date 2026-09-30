def analyze_number(n):
    digit_count = 0
    digit_sum = 0
    rev_num = 0
    temp = n
    
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        digit_count += 1
        rev_num = rev_num * 10 + digit
        temp = temp // 10
    
    is_even = (n % 2 == 0)
    
    return (digit_count, digit_sum, is_even, rev_num)


result = analyze_number(58372)
print(result)