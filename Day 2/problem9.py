num = int(input("Enter Number: "))

last_digit = num%10
first_digit = num//100

if first_digit == last_digit:
    print("Yes")
else:
    print("No")