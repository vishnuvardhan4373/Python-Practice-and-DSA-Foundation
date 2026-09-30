num = 12345
reversed_number = 0
while num > 0:
    digit = num % 10
    reversed_number = reversed_number * 10 + digit
    num = num // 10
print(f"Reversed Number is: {reversed_number}")