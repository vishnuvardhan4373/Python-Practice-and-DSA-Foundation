def perfect(n):
    total = 0
    if n < 2:
        return False
    for i in range(1,n):
        if n % i == 0:
            total += i
    is_perfect = (n == total)
    return is_perfect
n = int(input("Enter Number: "))
print(perfect(n))
