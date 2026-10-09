num = 1221
original = num
reversed_number = 0
while num > 0:
    digit = num % 10
    reversed_number = reversed_number * 10 + digit
    num = num // 10

if original == reversed_number:
    print(f"{original} is a Palindrome number.")
else:
    print(f"{original} is not a Palindrome number.")