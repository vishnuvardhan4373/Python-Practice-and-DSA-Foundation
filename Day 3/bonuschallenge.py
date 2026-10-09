n = int(input("Enter Number: "))
even_total = 0

while n > 0:
    digit = n % 10
    if digit %2 == 0:
        even_total += digit
    n = n // 10
print(even_total)