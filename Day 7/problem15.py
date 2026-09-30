numbers = [10, 45, 23, 89, 67, 89, 12]

largest = numbers[0]
second_largest = numbers[0]

for n in numbers:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print(f"Second largest = {second_largest}")