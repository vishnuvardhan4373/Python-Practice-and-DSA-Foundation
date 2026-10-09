def count_digits(num):
    count = 0
    digit = 0
    while num > 0:
        digit = num % 10
        count += 1
        num = num // 10
    return count
print("Number of Digits in the Given Number is:",count_digits(58372))