num = int(input("Enter the Number: "))
total = 0
last_digit = 0
while num >0:
    last_digit = num % 10
    total += last_digit
    num = num // 10
print(total)