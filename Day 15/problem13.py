def sum_n(n):
    if n <= 1:
        return 1
    total = n + sum_n(n-1)
    return total
print(sum_n(5))