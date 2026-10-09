def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
numbers = [1, 5, 8, 9, 4, 6, 17]
print("Sum of the Numbers in the Given List is:",sum_numbers(numbers))