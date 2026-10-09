numbers = [10, 5, 20, 8, 5, 15]
smallest = numbers[0]
second_smallest = numbers[1]
for number in numbers:
    if number < smallest:
        second_smallest = smallest
        smallest = number
    elif number < second_smallest and number != smallest:
        second_smallest = number
print("Second Smallgest:", second_smallest)