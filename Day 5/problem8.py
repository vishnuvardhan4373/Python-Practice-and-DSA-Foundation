numbers = [10, 5, 20, 8, 20, 15]
largest = numbers[0]
second_largest = numbers[1]
for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number
print("Second largest:", second_largest)