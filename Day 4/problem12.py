def sum_digits(num):
    total = 0
    digit = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total
num = int(input("Enter Number: "))
print("The Sum of the digits of Given Number is:",sum_digits(num))