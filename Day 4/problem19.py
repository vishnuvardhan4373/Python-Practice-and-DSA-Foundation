def armstrong(n):
    digit_cube = 0
    total_digit = 0
    original = n
    while n > 0:
        digit = n % 10
        digit_cube = digit * digit * digit
        total_digit += digit_cube
        n = n // 10
    is_armstrong = (original == total_digit)
    return is_armstrong
n = int(input("enter Number: "))
print(armstrong(n))