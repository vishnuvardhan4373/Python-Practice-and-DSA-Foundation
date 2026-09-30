numbers = [10, 3, 7, 8, 11, 4, 6]
total = 0
for num in numbers:
    if num %2 != 0:
        total += num
print(f"The Sum of Odd Numbers is: {total}")